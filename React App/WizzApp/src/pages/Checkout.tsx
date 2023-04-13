import { Button, Card, Col, Row, Steps, Typography, message } from 'antd';
import {
  AlignCenterOutlined,
  SolutionOutlined,
  LoadingOutlined,
  CreditCardOutlined,
  SmileOutlined
} from '@ant-design/icons';
import NavbarLayout from '~/layouts';
import { useState } from 'react';
const Checkout = () => {
  const [current, setCurrent] = useState(0);

  const next = () => {
    setCurrent(current + 1);
  };

  const prev = () => {
    setCurrent(current - 1);
  };

  const data = {};

  const steps = [
    {
      title: 'Flight Details',
      status: 'process',
      icon: <AlignCenterOutlined />,
      content: (
        <div>
          <Row>
            <Col span={12}>
              <div style={{ margin: 30 }}>
                <Typography.Title level={2}>Flight Details</Typography.Title>
                <Card title={''} style={{ width: 300 }}>
                  <p>Departure: </p>
                  <p>Arrival:</p>
                  <p>Date:</p>
                  <p>Passangers:</p>
                </Card>
              </div>
            </Col>
            <Col span={12}>
              <Row>
                <Typography.Title level={4}>
                  Destination events
                </Typography.Title>
              </Row>
              <Row>
                <Typography.Title level={4}>Transfers</Typography.Title>
              </Row>
              <Row>
                <Typography.Title level={4}>Hotels</Typography.Title>
              </Row>
            </Col>
          </Row>
        </div>
      )
    },
    {
      title: 'Verification',
      status: 'wait',
      icon: <SolutionOutlined />,
      content: <div></div>
    },
    {
      title: 'Pay',
      status: 'wait',
      icon: <CreditCardOutlined />,
      content: (
        <div>
          <p>Pay</p>
        </div>
      )
    },
    {
      title: 'Done',
      status: 'wait',
      icon: <SmileOutlined />,
      content: (
        <div>
          <p>Done</p>
        </div>
      )
    }
  ];

  const items = steps.map((item) => ({
    key: item.title,
    title: item.title,
    icon: item.icon
  }));

  return (
    <NavbarLayout>
      <div style={{ margin: 50 }}>
        <Steps items={items} current={current} />
        <div style={{ margin: 30 }}>{steps[current]?.content}</div>
        <div style={{ position: 'absolute', bottom: 75, right: '50%' }}>
          {current > 0 && (
            <Button
              size="large"
              style={{ margin: '0 8px' }}
              onClick={() => prev()}
            >
              Previous
            </Button>
          )}
          {current < steps.length - 1 && (
            <Button size="large" type="default" onClick={() => next()}>
              Next
            </Button>
          )}
          {current === steps.length - 1 && (
            <Button
              type="default"
              size="large"
              onClick={() => message.success('Processing complete!')}
            >
              Done
            </Button>
          )}
        </div>
      </div>
    </NavbarLayout>
  );
};

export default Checkout;
