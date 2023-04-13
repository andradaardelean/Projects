import { Row, Col, Button } from 'antd';
import { Header } from 'antd/es/layout/layout';
import type { FC, PropsWithChildren } from 'react';
import { Link } from 'react-router-dom';

interface NavbarLayoutProps {}

const NavbarLayout: FC<PropsWithChildren<NavbarLayoutProps>> = function ({
  children
}) {
  const MyHeader = () => {
    return (
      <Header className="header">
        <Row style={{ padding: 5 }}>
          <Col span={20}>
            <div>
              <Link to="/">
                <img src="wizz.png" alt="logo" width="200" height="60"></img>
              </Link>
            </div>
          </Col>
          <Col span={4}>
            <Link to="/signin">
              <Button
                type="default"
                style={{
                  justifyContent: 'center',
                  alignContent: 'center',
                  margin: '0 auto'
                }}
              >
                Sign in
              </Button>
            </Link>

            <Link to="/signup">
              <Button
                type="default"
                style={{
                  justifyContent: 'center',
                  alignContent: 'center',
                  marginLeft: 20
                }}
              >
                Sign up
              </Button>
            </Link>
          </Col>
        </Row>
      </Header>
    );
  };

  return (
    <div>
      <MyHeader />
      <div style={{ marginBottom: '180px' }}>{children}</div>
    </div>
  );
};

export default NavbarLayout;
