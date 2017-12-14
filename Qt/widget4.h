#ifndef WIDGET4_H
#define WIDGET4_H

#include <QWidget>

namespace Ui {
class Widget4;
}

class Widget4 : public QWidget
{
    Q_OBJECT

public:
    explicit Widget4(QWidget *parent = 0);
    ~Widget4();
    QString color;

private:
    Ui::Widget4 *ui;
    QVector<QPoint> points;
    int point_index;
    int xc,yc,rx,ry;

protected:
    void paintEvent(QPaintEvent *event);
    void timerEvent(QTimerEvent *event);

private slots:
    void on_pushButton_draw_clicked();
    void on_pushButton_draw_2_clicked();
    void on_comboBox_activated(const QString &arg1);
};

#endif // WIDGET4_H
