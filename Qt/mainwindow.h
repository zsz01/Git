#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "mainwidget.h"
#include "widget1.h"
#include "widget2.h"
#include "widget3.h"
#include "widget4.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private:
    Ui::MainWindow *ui;

private slots:
    void show_dda();
    void show_bresenham();
    void show_ellipse();
    void show_circle();

};

extern MainWindow *mw;

#endif // MAINWINDOW_H
