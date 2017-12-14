#include "mainwidget.h"
#include "ui_mainwidget.h"
#include "mainwindow.h"
#include "widget1.h"
#include "widget2.h"
#include "widget3.h"
#include "widget4.h"

Mainwidget::Mainwidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Mainwidget)
{
    ui->setupUi(this);
}

Mainwidget::~Mainwidget()
{
    delete ui;
}

void Mainwidget::on_button_1_clicked()
{
    mw->setCentralWidget(new Widget1);
}

void Mainwidget::on_button_2_clicked()
{
    mw->setCentralWidget(new Widget2);
}

void Mainwidget::on_button_3_clicked()
{
    mw->setCentralWidget(new Widget3);
}

void Mainwidget::on_button_4_clicked()
{
    mw->setCentralWidget(new Widget4);
}

