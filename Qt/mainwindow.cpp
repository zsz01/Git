#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <iostream>
#include <QApplication>
#include <QDesktopWidget>
#include <widget1.h>
#include <widget2.h>
#include <widget3.h>
#include <widget4.h>


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setWindowFlags(Qt::WindowMinimizeButtonHint | Qt::WindowCloseButtonHint);
    setFixedSize(768, 480);
    setGeometry((QApplication::desktop()->width()-width())/2,(QApplication::desktop()->height()-height())/2,width(),height());
    connect(ui->DDA,SIGNAL(triggered()),this,SLOT(show_dda()));
    connect(ui->Bresenham,SIGNAL(triggered()),this,SLOT(show_bresenham()));
    connect(ui->circle,SIGNAL(triggered()),this,SLOT(show_circle()));
    connect(ui->ellipse,SIGNAL(triggered()),this,SLOT(show_ellipse()));
}

void MainWindow::show_dda(){
    mw->setCentralWidget(new Widget1);
}

void MainWindow::show_bresenham(){
    mw->setCentralWidget(new Widget2);
}

void MainWindow::show_ellipse(){
    mw->setCentralWidget(new Widget4);
}

void MainWindow::show_circle(){
    mw->setCentralWidget(new Widget3);
}


MainWindow::~MainWindow()
{
    delete ui;
}
