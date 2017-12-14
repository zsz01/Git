#include "widget3.h"
#include "ui_widget3.h"
#include "mainwidget.h"
#include "mainwindow.h"
#include <QPainter>
#include <QPoint>
#include <QTimer>



Widget3::Widget3(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget3)
{
    ui->setupUi(this);
    ui->pushButton_draw->setShortcut(Qt::Key_Return);
    ui->pushButton_draw_2->setShortcut(Qt::Key_Escape);
    startTimer(3);
}

Widget3::~Widget3()
{
    delete ui;
}

void Widget3::paintEvent(QPaintEvent *event) {
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

    if(point_index == int(points.size())){
        if(color == "浅灰"){
            painter.setBrush(Qt::lightGray);
            painter.drawEllipse(cx + x0 - r , cy - y0 - r, 2*r, 2*r);
        }else if(color == "深黄"){
            painter.setBrush(Qt::darkYellow);
            painter.drawEllipse(cx + x0 - r , cy - y0 - r, 2*r, 2*r);
        }
    }
}

void Widget3::timerEvent(QTimerEvent *event){
    Q_UNUSED(event);
    repaint();
}


void Widget3::on_pushButton_draw_clicked()
{
    points.clear();
    point_index = 0;
    x0 = ui->lineEdit_x0->text().toInt();
    y0 = ui->lineEdit_y0->text().toInt();
    r = ui->lineEdit_r->text().toInt();
    int cx = (width() -200) / 2 + 200, cy = height() / 2;

    int x = 0, y = r, d = 5 / 4 - r;
    while (x <= y) {
        points.push_back(QPoint(cx + (x0 + x), cy - (y0 + y)));
        points.push_back(QPoint(cx + (x0 - x), cy - (y0 - y)));
        points.push_back(QPoint(cx + (x0 + x), cy - (y0 - y)));
        points.push_back(QPoint(cx + (x0 - x), cy - (y0 + y)));
        points.push_back(QPoint(cx + (x0 + y), cy - (y0 + x)));
        points.push_back(QPoint(cx + (x0 - y), cy - (y0 - x)));
        points.push_back(QPoint(cx + (x0 + y), cy - (y0 - x)));
        points.push_back(QPoint(cx + (x0 - y), cy - (y0 + x)));
        if (d >= 0) {
            x++;
            y--;
            d += 2 * (x - y) + 1;
        } else {
            x++;
            d += 2 * x + 1;
        }
    }
}

void Widget3::on_pushButton_draw_2_clicked()
{
    this->~Widget3();
    mw->setCentralWidget(new Mainwidget);
}


void Widget3::on_comboBox_currentIndexChanged(const QString &arg1)
{
    color = arg1;
}
