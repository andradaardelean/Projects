import { Button, Card, Form, Input, message } from 'antd';
import { useNavigate, Link } from 'react-router-dom';
import NavbarLayout from "../layouts";
import { useCreateUser } from "../state";
import { User, UserType } from "../types";
import './styles/AuthPage.css';
import { useState } from 'react';

const SignUp: React.FC = () => {
  const navigate = useNavigate();

  const { mutate: createUser } = useCreateUser();
  const [isLoading, setIsLoading]= useState(false);

  const onFinish = (values: any) => {
    setIsLoading(true);
    const user: User = {
      Id: "test",
      FirstName: values.fname,
      LastName: values.lname,
      Email: values.email,
      Password: values.password,
      Type: UserType.User
    }

    createUser(user, {
      onSuccess: () => {
        message.success('Account created successfully!')
        setIsLoading(false);
        navigate('/signin');
      },
      onError: (error: any) => {
        message.error('Account creation failed!' + error)
        setIsLoading(false);
      }
    });
  };

  const onFinishFailed = (errorInfo: any) => {
    console.log('Failed:', errorInfo);
  };

  return (
    <NavbarLayout tab="3">
    <div className="auth-page-container">
      <Card title="Sign Up Now!" className="auth-card">
        <Form
          style={{ marginBottom: '10px' }}
          // name="basic"
          layout="vertical"
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
          autoComplete="off"
        >
          <Form.Item
            label="First Name"
            name="fname"
            rules={[{ required: true, message: 'Please input your first name!' }]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            label="Last Name"
            name="lname"
            rules={[{ required: true, message: 'Please input your last name!' }]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            label="Email"
            name="email"
            rules={[{ required: true, message: 'Please input your email!' }]}
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
          <Form.Item
            name="confirm"
            label="Confirm Password"
            dependencies={['password']}
            hasFeedback
            rules={[
              {
                required: true,
                message: 'Please confirm your password!',
              },
              ({ getFieldValue }) => ({
                validator(_, value) {
                  if (!value || getFieldValue('password') === value) {
                    return Promise.resolve();
                  }
                  return Promise.reject(new Error('The two passwords that you entered do not match!'));
                },
              }),
            ]}
          >
            <Input.Password />
          </Form.Item>

          <Form.Item>
            <Button type="primary" htmlType="submit" block loading={isLoading}>
              Sign up
            </Button>
          </Form.Item>

          <Form.Item
            style={{ textAlign: 'right' }}>
              <Link to="/signin">Already have an account?</Link>
            </Form.Item>
        </Form>
        </Card>
      </div>
    </NavbarLayout>
  );
};

export default SignUp;
