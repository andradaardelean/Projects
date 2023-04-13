import { Button, Card, Modal, Typography } from 'antd';
import { useLocation, useNavigate } from 'react-router-dom';
import NavbarLayout from '~/layouts';
import { queryToObject } from '~/utils/utils';

const FlightPage = () => {
  const { search } = useLocation();
  const navigate = useNavigate();
  // api
  const user = {};
  const isAuth = false;

  const data = queryToObject(search);

  const handleBuy = () => {
    if (!isAuth) {
      warning();
    } else {
      // api
      navigate('/checkout');
    }
  };

  const warning = () => {
    Modal.warning({
      title: 'You need to sign in first!',
      content: 'You need to sign in first to buy this flight.',
      onOk() {
        navigate('/signin');
      }
    });
  };

  return (
    <NavbarLayout>
      <div style={{ margin: 30 }}>
        <Typography.Title level={2}>Flight Details</Typography.Title>
        <Card
          title={data?.['departure'] + ' - ' + data?.['destination']}
          extra={<a href="#">More</a>}
          style={{ width: 300 }}
          actions={[
            <Button type="primary" onClick={handleBuy}>
              Buy
            </Button>
          ]}
        >
          <p>Departure: {data?.['departure']}</p>
          <p>Arrival: {data?.['destination']}</p>
          <p>Date: {data?.['date']}</p>
          <p>Passangers: {data?.['passengers']}</p>
        </Card>
      </div>
    </NavbarLayout>
  );
};

export default FlightPage;
