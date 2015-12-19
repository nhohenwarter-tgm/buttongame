#include "buttongameview.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    ButtonGameView w;
    w.show();

    return a.exec();
}
