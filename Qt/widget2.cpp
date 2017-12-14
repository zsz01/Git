#include "widget2.h"
#include "ui_widget2.h"
#include "mainwindow.h"
#include "mainwidget.h"
#include <QPainter>
#include <QPoint>

Widget2::Widget2(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget2)
{
    ui->setupUi(this);
    ui->pushButton_draw->setShortcut(Qt::Key_Return);
    ui->pushButton_draw_2->setShortcut(Qt::Key_Escape);
    startTimer(3);
}

Widget2::~Widget2()
{
    delete ui;
}


void Widget2::paintEvent(QPaintEvent *event) {
    Q_UNUSED(event);
    QPainter painter(this);
    painter.setPen(Qt::black);
    int cx = (width() -200) / 2 + 200, cy = height() / 2;

    //define the boundary
    int x_min = (width()-200) / 16 + 200 , x_max = (width()-200) / 16 * 15 + 200;
    int y_min = height() / 16, y_max = height() / 16 * 15;

    //200 represent the boundary to the left
    painter.drawLine(QPoint(cx, y_min), QPoint(cx, y_max));
    painter.drawLine(QPoint(x_min, cy), QPoint(x_max , cy));

    //draw the coord
    QPoint P(cx,cy);
    for(QPoint i = P; i.x() >= x_min; i.setX(i.x() - 50)){
        painter.drawLine(i,QPoint(i.x(),i.y()-2));
    }
    for(QPoint i = P; i.x() <= x_max; i.setX(i.x() + 50)){
        painter.drawLine(i,QPoint(i.x(),i.y()-2));
    }
    for(QPoint i = P; i.y() >=y_min; i.setY(i.y() - 50)){
        painter.drawLine(i,QPoint(i.x()+2,i.y()));
    }
    for(QPoint i = P; i.y() <= y_max; i.setY(i.y() + 50)){
        painter.drawLine(i,QPoint(i.x()+2,i.y()));
    }

    //draw the scale
    painter.drawText(QPoint(cx - 12,cy + 15),"0");  //norm primitive point
    painter.drawText(QPoint(cx - 12 - 50,cy + 15),"-50");
    painter.drawText(QPoint(cx - 12 - 105,cy + 15),"-100");
    painter.drawText(QPoint(cx - 12 - 155,cy + 15),"-150");
    painter.drawText(QPoint(cx - 12 - 205,cy + 15),"-200");

    painter.drawText(QPoint(cx - 12 + 56,cy + 15),"50");
    painter.drawText(QPoint(cx - 12 + 101,cy + 15),"100");
    painter.drawText(QPoint(cx - 12 + 151,cy + 15),"150");
    painter.drawText(QPoint(cx - 12 + 201,cy + 15),"200");

    painter.drawText(QPoint(cx - 18,cy + 15 - 60),"50");
    painter.drawText(QPoint(cx - 25,cy + 15 - 110),"100");
    painter.drawText(QPoint(cx - 25,cy + 15 - 160),"150");
    painter.drawText(QPoint(cx - 25,cy + 15 - 210),"200");

    painter.drawText(QPoint(cx - 25,cy + 15 + 40),"-50");
    painter.drawText(QPoint(cx - 32,cy + 15 + 90),"-100");
    painter.drawText(QPoint(cx - 32,cy + 15 + 140),"-150");
    painter.drawText(QPoint(cx - 32,cy + 15 + 190),"-200");


    //draw the arrows

    painter.drawLine(QPoint(cx, y_min), QPoint(cx - 3 , y_min + 9));
    painter.drawLine(QPoint(cx, y_min), QPoint(cx + 3 , y_min + 9));
    painter.drawLine(QPoint(x_max - 9 , cy - 3), QPoint(x_max, cy));
    painter.drawLine(QPoint(x_max - 9 , cy + 3), QPoint(x_max, cy));

    painter.drawLine(QPoint(cx, y_min), QPoint(cx - 2 , y_min + 9));
    painter.drawLine(QPoint(cx, y_min), QPoint(cx + 2 , y_min + 9));
    painter.drawLine(QPoint(x_max - 9 , cy - 2), QPoint(x_max, cy));
    painter.drawLine(QPoint(x_max - 9 , cy + 2), QPoint(x_max, cy));

    painter.drawLine(QPoint(cx, y_min), QPoint(cx - 1 , y_min + 9));
    painter.drawLine(QPoint(cx, y_min), QPoint(cx + 1 , y_min + 9));
    painter.drawLine(QPoint(x_max - 9 , cy - 1), QPoint(x_max, cy));
    painter.drawLine(QPoint(x_max - 9 , cy + 1), QPoint(x_max, cy));

    //draw the central point
    painter.drawEllipse(cx-1, cy-1, 2, 2);
    painter.drawEllipse(cx-2, cy-2, 4, 4);

    painter.drawPoints(&points[0],point_index);
    point_index = std::min(point_index + 1, int(points.size()));

}


void Widget2::timerEvent(QTimerEvent *event){
    Q_UNUSED(event);
    repaint();
}


void Widget2::on_pushButton_draw_clicked()
{
    points.clear();
    point_index = 0;

    int x1 = ui->lineEdit_x1->text().toInt(), y1 = ui->lineEdit_y1->text().toInt();
    int x2 = ui->lineEdit_x2->text().toInt(), y2 = ui->lineEdit_y2->text().toInt();
    int cx = (width() -200) / 2 + 200, cy = height() / 2;

    int dx = x2 - x1, dy = y2 - y1;
    int ux = dx > 0 ? 1 : -1, uy = dy > 0 ? 1 : -1;
    int x = x1, y = y1, eps = 0;
    dx = abs(dx);
    dy = abs(dy);
    if(lineshape != "虚线"){
        if (dx > dy) {
            for (x = x1; x != x2 + ux; x += ux) {
                points.push_back(QPoint(cx + x, cy - y));
                eps += dy;
                if (eps * 2 >= dx) {
                    y += uy;
                    eps -= dx;
                }
            }
        } else {
            for (y = y1; y != y2 + uy; y += uy) {
                points.push_back(QPoint(cx + x, cy - y));
                eps += dx;
                if (eps * 2 >= dy) {
                    x += ux;
                    eps -= dy;
                }
            }
        }
    }else{
        bool lineflag = true;
        if (dx > dy) {
            for (x = x1; x != x2 + ux; x += ux) {
                if((lineflag = !lineflag)){
                    points.push_back(QPoint(cx + x, cy - y));
                }
                eps += dy;
                if (eps * 2 >= dx) {
                    y += uy;
                    eps -= dx;
                }
            }
        } else {
            for (y = y1; y != y2 + uy; y += uy) {
                if((lineflag = !lineflag)){
                    points.push_back(QPoint(cx + x, cy - y));
                }
                eps += dx;
                if (eps * 2 >= dy) {
                    x += ux;
                    eps -= dy;
                }
            }
        }
    }
}

void Widget2::on_pushButton_draw_2_clicked()
{
    this->~Widget2();
    mw->setCentralWidget(new Mainwidget);
}

void Widget2::on_comboBox_activated(const QString &arg1)
{
    lineshape = arg1;
}


