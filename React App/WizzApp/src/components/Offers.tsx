import { Row, Col, Card, Spin } from 'antd';
import Meta from 'antd/es/card/Meta';
import { useGetData } from '~/state';

const Offers = () => {
  const { data: flightData, isLoading } = useGetData();

  if (isLoading) return <Spin />;

  if (!flightData) return null;

  return (
    <div style={{ margin: 100 }}>
      <Row gutter={[16, 16]}>
        {flightData.map((flight: any) => (
          <Col span={6}>
            <Card
              hoverable
              style={{ width: 240 }}
              cover={<img alt="example" src="PowerfulReasons_hero.jpg" />}
            >
              <Meta
                title={flight.arrival?.timezone}
                description={
                  <div>
                    <div>Airline: {flight.airline?.name}</div>
                    <div>Departure: {flight.departure?.airport}</div>
                    <div>Destination: {flight.arrival?.airport}</div>
                    <div>Flight date: {flight.flight_date}</div>
                    <div>Status {flight.flight_status}</div>
                    <div>Price: {flight.price ?? 'Just $19.99!'}</div>
                  </div>
                }
              />
            </Card>
          </Col>
        ))}
      </Row>
    </div>
  );
};

export default Offers;
