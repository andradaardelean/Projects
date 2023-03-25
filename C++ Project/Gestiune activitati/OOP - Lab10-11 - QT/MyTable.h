//
// Created by Laura on 6/2/2022.
//

#ifndef UNTITLED_MYTABLEMODEL_H
#define UNTITLED_MYTABLEMODEL_H
#include <QAbstractTableModel>
#include <QBrush>
#include <Qt>
#include <QFont>
#include "domain.h"
#include <vector>
#include <qdebug.h>
using std::vector;


class MyTableModel :public QAbstractTableModel {
    std::vector<Activitate> activity;
public:
    MyTableModel(const std::vector<Activitate>& prod) :activity{ prod } {
    }

    int rowCount(const QModelIndex& parent = QModelIndex()) const override {
        return activity.size();
    }
    int columnCount(const QModelIndex& parent = QModelIndex()) const override {
        return 4;
    }
    //Returns the data stored under the given role for the item referred to by the index.
    QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override {
        if (role == Qt::ForegroundRole) {
            auto prod = this->activity[index.row()];
            if (prod.get_durata() > 200) {
                return QBrush(Qt::darkGreen);
            }
        }
        if (role == Qt::FontRole) {
            QFont f;
            f.setItalic(index.row() % 10 == 0);
            f.setBold(index.row() % 10 == 3);
            return f;
        }
        if (role == Qt::BackgroundRole) {

            int row = index.row();
            QModelIndex i = index.sibling(index.row(), 1);
            if (i.data().toString() == "cosmetic") {
                QBrush bg(Qt::darkRed);
                return bg;
            }
        }

        if (role == Qt::DisplayRole) {

            Activitate p = activity[index.row()];
            if (index.column() == 0) {
                return QString::fromStdString(p.get_titlu());
            }
            else if (index.column() == 1) {
                return QString::fromStdString(p.get_descriere());
            }
            else if (index.column() == 2) {
                return QString::fromStdString(p.get_tip());
            }
            else if (index.column() == 3) {
                return QString::number(p.get_durata());
            }
        }

        return QVariant{};
    }

    void setAct(const vector<Activitate> prod) {
        this->activity = prod;
        auto topLeft = createIndex(0, 0);
        auto bottomR = createIndex(rowCount(), columnCount());
        emit dataChanged(topLeft, bottomR);
        emit layoutChanged();
    }

    Qt::ItemFlags flags(const QModelIndex& /*index*/) const {
        return Qt::ItemIsSelectable | Qt::ItemIsEditable | Qt::ItemIsEnabled;
    }

    QVariant headerData(int section, Qt::Orientation orientation, int role) const
    {
        if (role == Qt::DisplayRole)
        {
            if (orientation == Qt::Horizontal) {
                switch (section)
                {
                case 0:
                    return tr("Nume");
                case 1:
                    return tr("Tip");
                case 2:
                    return tr("Producator");
                case 3:
                    return tr("Pret");
                default:
                    return QString("");
                }
            }
        }
        return QVariant();
    }
};
#endif //UNTITLED_MYTABLEMODEL_H
