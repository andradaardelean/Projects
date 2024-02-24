import { Tabs, message } from 'antd';
import { Header } from 'antd/es/layout/layout';
import { FC, PropsWithChildren, useEffect, useState } from 'react';
import { HomeOutlined, HeartOutlined, LoginOutlined, LogoutOutlined, PlusCircleOutlined, UserAddOutlined, CarOutlined } from '@ant-design/icons';
import { useNavigate } from 'react-router-dom';
import { useLogOut } from "../state";
import Cookies from 'js-cookie';

interface Props {
  tab?: string;
}

const NavbarLayout: FC<PropsWithChildren<Props>> = function ({
  children, tab
}) {
  const navigate = useNavigate();
  const { mutate: logOut } = useLogOut();
  const [userType] = useState<string>(Cookies.get('userType') ?? "");
  const [tabItems, setTabItems] = useState<any[]>([]);

  useEffect(() => {
    if (userType === '0') {
      setTabItems([{ icon: CarOutlined, title: 'Tasks', link: '/employee' }, { icon: PlusCircleOutlined, title: "Add Center", link: "/center" }, { icon: LogoutOutlined, title: 'Log Out', link: '/home' }]);
    } else if (userType === '1') {
      setTabItems([{ icon: HomeOutlined, title: 'Home', link: '/home' }, { icon: HeartOutlined, title: 'Make a Donation', link: '/donation' }, { icon: LogoutOutlined, title: 'Log Out', link: '/home' }]);
    } else {
      setTabItems([{ icon: HomeOutlined, title: 'Home', link: '/home' }, { icon: LoginOutlined, title: 'Sign In', link: '/signin' }, { icon: UserAddOutlined, title: 'Sign up', link: '/signup' }]);
    }
  }, [Cookies.get('userType')]);

  const MyHeader = () => {
    return (
      <Header style={{ backgroundColor: "#1AA6B7" }}>
        <Tabs
          defaultActiveKey={tab || '1'}
          style={{ float: 'right' }}
          items={tabItems.map((tabItem, i) => {
            const id = String(i + 1);

            if (tabItem.title === 'Log Out') {
              return {
                label: (
                  <span onClick={() => {
                    logOut(null, {
                      onSuccess: () => {
                        Cookies.remove('userId');
                        Cookies.remove('userType');
                        message.success('Logged out successfully!');
                        navigate(tabItem.link);
                        window.location.reload();

                      },
                      onError: (error: any) => {
                        console.log('Log out failed!' + error);
                      }
                    });
                  }}>
                    <tabItem.icon />
                    {tabItem.title}
                  </span>
                ),
                key: id,
              };
            }
            return {
              label: (
                <span onClick={() => {
                  navigate(tabItem.link)
                }} >
                  <tabItem.icon />
                  {tabItem.title}
                </span>
              ),
              key: id,
            };
          })}
        />

      </Header >
    );
  };

  return (
    <div>
      <MyHeader />
      <div style={{ marginBottom: '180px' }}>{children}</div>
      <footer>
        <p>&copy; 2023 Santa For A Day. | All rights reserved.</p>
        <nav>
          <ul>
            <li><a href="contact.html">Contact Us</a></li>
            <li><a href="privacy.html">Privacy Policy</a></li>
            <li><a href="terms.html">Terms of Service</a></li>
          </ul>
        </nav>
      </footer>
    </div>
  );
};

export default NavbarLayout;
