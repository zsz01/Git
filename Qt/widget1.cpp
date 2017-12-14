#include "widget1.h"
#include "ui_widget1.h"
#include "mainwindow.h"
#include "mainwidget.h"
#include "QPainter"
#include <cmath>
#include <QPoint>

Widget1::Widget1(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget1) {
    ui->setupUi(this);
    ui->pushButton_draw->setShortcut(Qt::Key_Return);
    ui->pushButton_draw_2->setShortcut(Qt::Key_Escape);
    startTimer(3);
}

Widget1::~Widget1() {
    delete ui;
}


void Widget1::paintEvent(QPaintEvent *event) {
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

void Widget1::timerEvent(QTimerEvent *event){
    Q_UNUSED(event);
    repaint();
}

void Widget1::on_pushButton_draw_clicked() {
    points.clear();
    point_index = 0;
    int x1 = ui->lineEdit_x1->text().toInt(), y1 = ui->lineEdit_y1->text().toInt();
    int x2 = ui->lineEdit_x2->text().toInt(), y2 = ui->lineEdit_y2->text().toInt();
    int cx = (width() -200) / 2 + 200, cy = height() / 2;

    int dx = x2 - x1, dy = y2 - y1, steps = std::max(abs(dx), abs(dy));
    double x_inc = double(dx) / double(steps), y_inc = double(dy) / double(steps), x = x1, y = y1;
    points.push_back(QPoint(cx + int (round(x)), cy - int (round(y))));

    if(lineshape == "虚线"){
        for (int k = 0; k < steps; k++) {
            x += x_inc;
            y += y_inc;
            if(k % 2){
                points.push_back(QPoint(cx + int (round(x)), cy - int (round(y))));
            }
        }
    }else{
        for (int k = 0; k < steps; k++) {
            x += x_inc;
            y += y_inc;
            points.push_back(QPoint(cx + int (round(x)), cy - int (round(y))));
        }
    }

}

void Widget1::on_pushButton_draw_2_clicked()
{
    this->~Widget1();
    mw->setCentralWidget(new Mainwidget);
}

void Widget1::on_comboBox_activated(const QString &arg1)
{
    lineshape = arg1;
}

