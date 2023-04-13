import { Button, Form, Input } from 'antd';
import { useNavigate } from 'react-router-dom';
import NavbarLayout from '~/layouts';

const Signin: React.FC = () => {
  const navigate = useNavigate();

  const onFinish = (_values: any) => {
    navigate('/');
  };

  const onFinishFailed = (errorInfo: any) => {
    console.log('Failed:', errorInfo);
  };

  return (
    <NavbarLayout>
      <div
        style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          height: '100vh'
        }}
      >
        <Form
          name="basic"
          layout="vertical"
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
          autoComplete="off"
        >
          <Form.Item
            label="Username"
            name="username"
            rules={[{ required: true, message: 'Please input your username!' }]}
          >
            <Input />
          </Form.Item>

          <Form.Item
            label="Password"
            name="password"
            rules={[{ required: true, message: 'Please input your password!' }]}
          >
            <Input.Password />
          </Form.Item>

          <Form.Item>
            <Button type="primary" htmlType="submit" block>
              Sign up!
            </Button>
          </Form.Item>
        </Form>
      </div>
    </NavbarLayout>
  );
};

export default Signin;
