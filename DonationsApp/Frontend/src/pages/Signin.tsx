import { Button, Card, Form, Input, message } from 'antd';
import NavbarLayout from '../layouts';
import './styles/AuthPage.css';
import { useLogIn } from '../state';
import { useState } from 'react';
import Cookies from 'js-cookie';

const SignIn: React.FC = () => {
	const { mutate: logIn } = useLogIn();
	const [isLoading, setIsLoading] = useState(false);

	const onFinish = (values: any) => {
		setIsLoading(true);
		const authUser = {
			Email: values.email,
			Password: values.password,
		};
		logIn(authUser, {
			onSuccess: (response) => {
				console.log(response);
				Cookies.set('userId', response.data.id);
				Cookies.set('userType', response.data.type);
				setIsLoading(false);
				message.success('Logged in successfully!');
				window.location.reload();
			},

			onError: (error: any) => {
				message.error('Log in failed!' + error);
				setIsLoading(false);
			},
		});
	};

	const onFinishFailed = (errorInfo: any) => {
		console.log('Failed:', errorInfo);
	};

	return (
		<NavbarLayout tab='2'>
			<div className='auth-page-container'>
				<Card
					title='Enter your credentials to sign in'
					className='auth-card'>
					<Form
						name='basic'
						layout='vertical'
						onFinish={onFinish}
						onFinishFailed={onFinishFailed}
						autoComplete='off'
						style={{ marginBottom: '100px' }}>
						<Form.Item
							label='Email'
							name='email'
							rules={[
								{ required: true, message: 'Please input your email!' },
							]}>
							<Input />
						</Form.Item>

						<Form.Item
							label='Password'
							name='password'
							rules={[
								{ required: true, message: 'Please input your password!' },
							]}>
							<Input.Password />
						</Form.Item>

						<Form.Item>
							<Button type='primary' htmlType='submit' loading={isLoading} block>
								Sign in
							</Button>
						</Form.Item>
					</Form>
				</Card>
			</div>
		</NavbarLayout>
	);
};

export default SignIn;
