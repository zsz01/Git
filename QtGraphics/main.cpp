#include "mainwindow.h"
#include "mainwidget.h"
#include <QApplication>
#include <iostream>
#include <QString>
MainWindow *mw;
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    mw = new MainWindow;
    mw->show();
    mw->setCentralWidget(new Mainwidget);
    return a.exec();
}
