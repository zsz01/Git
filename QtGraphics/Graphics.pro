#-------------------------------------------------
#
# Project created by QtCreator 2017-10-05T15:48:41
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = Graphics
TEMPLATE = app

# The following define makes your compiler emit warnings if you use
# any feature of Qt which as been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

CONFIG += c++14

SOURCES += \
        main.cpp \
        mainwindow.cpp \
    widget1.cpp \
    widget2.cpp \
    widget3.cpp \
    widget4.cpp \
    mainwidget.cpp

HEADERS += \
        mainwindow.h \
    widget1.h \
    widget2.h \
    widget3.h \
    widget4.h \
    mainwidget.h

FORMS += \
        mainwindow.ui \
    widget1.ui \
    widget2.ui \
    widget3.ui \
    widget4.ui \
    mainwidget.ui

