#ifndef BUTTONGAMEVIEW_H
#define BUTTONGAMEVIEW_H

#include <QMainWindow>

namespace Ui {
class ButtonGameView;
}

class ButtonGameView : public QMainWindow
{
    Q_OBJECT

public:
    explicit ButtonGameView(QWidget *parent = 0);
    ~ButtonGameView();

private:
    Ui::ButtonGameView *ui;
};

#endif // BUTTONGAMEVIEW_H
