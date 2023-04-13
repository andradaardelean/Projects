import { Row, Col } from "antd";
import { Footer, Header } from "antd/es/layout/layout";
import type { FC, PropsWithChildren } from "react";

interface NavbarLayoutProps { }

const NavbarLayout: FC<PropsWithChildren<NavbarLayoutProps>> = function ({
  children,
}) {
  const MyHeader = () => {
    return (
      <Header className="header">
        <div className="logo" />
        <Row>
          <Col span={1}><div>
            <img src="wizz.png" alt="logo" width="200" height="60" ></img>
          </div></Col>
        </Row>
      </Header>
    )
  }

  return (
    <div>
      <MyHeader />
      <div style={{ marginBottom: "180px" }}>{children}</div>
      <Footer style={{ textAlign: 'center' }}>Ant Design ©2023 Created by Ant UED</Footer>
    </div>
  );
};

export default NavbarLayout;