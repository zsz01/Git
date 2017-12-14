#ifndef MAINWIDGET_H
#define MAINWIDGET_H

#include <QWidget>

namespace Ui {
class Mainwidget;
}

class Mainwidget : public QWidget
{
    Q_OBJECT

public:
    explicit Mainwidget(QWidget *parent = 0);
    ~Mainwidget();

private slots:
    void on_button_1_clicked();
    void on_button_2_clicked();
    void on_button_3_clicked();
    void on_button_4_clicked();
private:
    Ui::Mainwidget *ui;
};

#endif // MAINWIDGET_H
