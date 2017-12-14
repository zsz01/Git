#ifndef WIDGET1_H
#define WIDGET1_H

#include <QWidget>

namespace Ui {
class Widget1;
}

class Widget1 : public QWidget
{
    Q_OBJECT

public:
    explicit Widget1(QWidget *parent = 0);
    ~Widget1();
    QString lineshape;

private slots:
    void on_pushButton_draw_clicked();
    void on_pushButton_draw_2_clicked();
    void on_comboBox_activated(const QString &arg1);

private:
    Ui::Widget1 *ui;
    QVector<QPoint> points;
    int point_index;

protected:
    void paintEvent(QPaintEvent *event);
    void timerEvent(QTimerEvent *event);
};

#endif // WIDGET1_H
