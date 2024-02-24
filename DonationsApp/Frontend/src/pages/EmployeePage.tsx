import { message, Button, Col, Row, Typography, Table, Tag } from "antd";
import NavbarLayout from "../layouts/index";
import { useAssignTask, useCompleteTask, useGetMyCompletedTasks, useGetMyInProgressTasks, useGetTasks } from "../state/index";
import { ColumnsType } from "antd/es/table";
import { useState } from "react";
const { Title } = Typography;

const EmployeePage = () => {
  const { data: tasks, refetch: refetchTasks } = useGetTasks();

  const { data: myInProgresssTasks, refetch: refetchMyInProgressTasks } = useGetMyInProgressTasks();  // sa se faca update-uri la query cand se face mutate
  const { data: myCompletedTasks, refetch: refetchMyCompletedTasks } = useGetMyCompletedTasks();
  const { mutate: assignTask } = useAssignTask();
  const { mutate: completeTask } = useCompleteTask();

  const [task, setTask] = useState<any>(null);
  const [ipTask, setIPTask] = useState<any>(null);

  const columns: ColumnsType<any> = [
    {
      title: 'Donor address',
      dataIndex: 'donation',
      render(donation: any) {
        return donation.donator.homeAddress;
      }
    },
    {
      title: 'Gift',
      dataIndex: 'donation',
      render(donation: any) {
        return donation.giftDescription;
      }
    },
    {
      title: "Status",
      dataIndex: 'donationTaskStatus',
      render(text: any) {
        switch (text) {
          case 0:
            return <Tag color="warning">Created</Tag>
          case 1:
            return <Tag color="blue">Pending</Tag>
          case 2:
            return <Tag color="green">Completed</Tag>
          default:
            return <Tag></Tag>
        }
      }
    }
  ];

  const rowSelection = {
    onChange: (selectedRowKeys: React.Key[], selectedRows: any) => {
      setTask(selectedRows[0] ?? selectedRows);
      console.log(`selectedRowKeys: ${selectedRowKeys}`, 'selectedRows: ', selectedRows);
    },
    getCheckboxProps: (record: any) => ({
      disabled: record.empoyeeId
    }),
  };

  const rowIPSelection = {
    onChange: (selectedRowKeys: React.Key[], selectedRows: any) => {
      setIPTask(selectedRows[0] ?? selectedRows);
      console.log(`selectedRowKeys: ${selectedRowKeys}`, 'selectedRows: ', selectedRows);
    },
  };

  const handleAssignTask = () => {
    assignTask(task.id, {
      onSuccess: () => {
        refetchTasks(); // Refetch the tasks query to get the updated data
        refetchMyInProgressTasks(); // Refetch the in-progress tasks query to get the updated data
        setTask(null);
        message.success('Task assigned successfully!')
      },
      onError: (error: any) => {
        message.error('Task assignment failed!' + error)
      }
    });
  }

  const handleCompleteTask = () => {
    completeTask(ipTask.id, {
      onSuccess: () => {
        refetchMyInProgressTasks(); // Refetch the in-progress tasks query to get the updated data
        refetchMyCompletedTasks(); // Refetch the completed tasks query to get the updated data
        setIPTask(null);
        message.success('Task completed successfully!')
      },
      onError: (error: any) => {
        message.error('Task completed failed!' + error)
      }
    });
  }

  return (
    <NavbarLayout tab="1">
      <Row>
        <Col span={8} style={{ padding: 6 }}>
          <Title level={2}>All Tasks
            <span style={{ marginLeft: 4 }}>- {tasks?.data.length}</span></Title>
          <Table
            columns={columns}
            dataSource={tasks?.data.map((task: any) => {
              return {
                ...task,
                key: task.id,
              }
            })}
            rowSelection={{
              type: "radio",
              ...rowSelection,
            }}
            pagination={false}
          />
          <Button disabled={!task} type="primary" style={{ marginTop: 4 }} block onClick={handleAssignTask}>Assign</Button>
        </Col>
        <Col span={8} style={{ padding: 6 }}>
          <Title level={2}>In Progress Tasks
            <span style={{ marginLeft: 4 }}>- {myInProgresssTasks?.data.length}</span></Title>
          <Table
            columns={columns}
            dataSource={myInProgresssTasks?.data.map((task: any) => {
              return {
                ...task,
                key: task.id,
              }
            })}
            rowSelection={{
              type: "radio",
              ...rowIPSelection,
            }}
            pagination={false}
          />
          <Button disabled={!ipTask} type="primary" style={{ marginTop: 4 }} block onClick={handleCompleteTask}>Complete</Button>
        </Col>
        <Col span={8} style={{ padding: 6 }}>
          <Title level={2}>Completed Tasks  <span style={{ marginLeft: 4 }}>- {myCompletedTasks?.data.length}</span></Title>
          <Table
            columns={columns}
            dataSource={myCompletedTasks?.data}
            pagination={false}
          />
        </Col>
      </Row>
    </NavbarLayout>
  );

}

export default EmployeePage;