#include "program.h"
#include "observer.h"
#include "service.h"
#include <qwidget.h>
#include <qpushbutton.h>
#include <qtablewidget.h>
#include <qslider.h>
#include <qlayout.h>
#include <vector>
#include "MyTable.h"

using std::vector;

class programCRUD_GUI : public QWidget, public Observer {
private:
	Program& program;
	ActivitateStore& srv;
	QWidget* main;
	QHBoxLayout* layout;
	QSlider* slider;
	QTableView* table;
	QPushButton* btnAdd;
	QPushButton* btnEmpty;

	MyTableModel* model;

	void initComponents();
	void connectSignals();

	//void populateTable(QTableWidget* table, vector<Activitate>& all);
	void populateTable(QTableView* table, const vector<Activitate>& all);
public:
	explicit programCRUD_GUI(Program& program, ActivitateStore& srv) : program{ program }, srv{ srv }{
		main = new QWidget;
		layout = new QHBoxLayout;
		btnAdd = new QPushButton("Generare activitati random");
		btnEmpty = new QPushButton("Goleste program");
		slider = new QSlider;
		table = new QTableView;
		this->model = new MyTableModel{srv.get_all_program_srv()};
	};

	void run();

	void update() override;

	~programCRUD_GUI() {
		this->program.removeObserver(this);
	}
};

//class programTABLE_GUI : public QWidget, public Observer {
//private:
//	Program& p;
//	QTableWidget* table;
//	QPushButton* btnEmpty;
//	void initGUI() {
//		QHBoxLayout* ly = new QHBoxLayout{};
//		this->setLayout(ly);
//		table = new QTableWidget{};
//		btnEmpty = new QPushButton{ "Goleste program" };
//		ly->addWidget(table);
//		ly->addWidget(btnEmpty);
//		setAttribute(Qt::WA_DeleteOnClose);
//		p.addObserver(this);
//	};
//
//	void reloadTableData(const vector<Activitate>& activities) {
//		this->table->setColumnCount(4);
//		this->table->setRowCount(activities.size());
//		for (int i = 0; i < activities.size(); i++) {
//			table->setItem(i, 0, new QTableWidgetItem(QString::fromStdString(activities[i].get_titlu())));
//			table->setItem(i, 1, new QTableWidgetItem(QString::fromStdString(activities[i].get_descriere())));
//			table->setItem(i, 2, new QTableWidgetItem(QString::fromStdString(activities[i].get_tip())));
//			table->setItem(i, 3, new QTableWidgetItem(QString::number(activities[i].get_durata())));
//		}
//	};
//
//	void connectSignalSlots() {
//		p.addObserver(this);
//
//		QObject::connect(btnEmpty, &QPushButton::clicked, [&]() {
//			p.goleste_program();
//			reloadTableData(p.get_all_from_program());
//			});
//	}
//
//public:
//	programTABLE_GUI(Program& p) :p{ p } {
//		initGUI();
//		connectSignalSlots();
//	};
//
//	void update() override {
//		this->reloadTableData(p.get_all_from_program());
//	}
//
//	~programTABLE_GUI() {
//		p.removeObserver(this);
//	}
//};







