#include "buttongameview.h"
#include "ui_buttongameview.h"

ButtonGameView::ButtonGameView(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::ButtonGameView)
{
    ui->setupUi(this);
}

ButtonGameView::~ButtonGameView()
{
    delete ui;
}
