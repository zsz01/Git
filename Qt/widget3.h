#ifndef WIDGET3_H
#define WIDGET3_H

#include <QWidget>

namespace Ui {
class Widget3;
}

class Widget3 : public QWidget
{
    Q_OBJECT

public:
    explicit Widget3(QWidget *parent = 0);
    ~Widget3();
    QString color;

private:
    Ui::Widget3 *ui;
    QVector<QPoint> points;
    int point_index;
    int x0,y0,r;

protected:
    void paintEvent(QPaintEvent *event);
    void timerEvent(QTimerEvent *event);

private slots:
    void on_pushButton_draw_clicked();
    void on_pushButton_draw_2_clicked();
    void on_comboBox_currentIndexChanged(const QString &arg1);
};

#endif // WIDGET3_H
