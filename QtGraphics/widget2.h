#ifndef WIDGET2_H
#define WIDGET2_H

#include <QWidget>

namespace Ui {
class Widget2;
}

class Widget2 : public QWidget
{
    Q_OBJECT

public:
    explicit Widget2(QWidget *parent = 0);
    ~Widget2();
    QString lineshape;

private slots:
    void on_pushButton_draw_clicked();
    void on_pushButton_draw_2_clicked();
    void on_comboBox_activated(const QString &arg1);

private:
    Ui::Widget2 *ui;
    QVector<QPoint> points;
    int point_index;

protected:
    void paintEvent(QPaintEvent *event);
    void timerEvent(QTimerEvent *event);
};

#endif // WIDGET2_H
