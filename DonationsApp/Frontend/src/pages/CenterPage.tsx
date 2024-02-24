import { Button, Card, Form, Input, message } from "antd"
import NavbarLayout from "../layouts"
import { useCreateCenter } from "../state/index";
import { useState } from "react";


const CenterPage = () => {
    const [form] = Form.useForm();
    const [isLoading, setIsLoading] = useState<any>(false);
    const { mutate: createCenter } = useCreateCenter();

    const onFinish = (values: any) => {
        setIsLoading(true);
        const center: any = {
            State: values.state,
            City: values.city,
            Name: values.name,
            Address: values.address,
        }

        createCenter(center, {
            onSuccess: () => {
                message.success('Center created successfully!')
                form.resetFields();
            },
            onError: (error: any) => {
                message.error('Center creation failed!' + error)
            }
        });
        setIsLoading(false);
    };
    return (
        <NavbarLayout tab={"2"}>
            <div className="auth-page-container">
                <Card title="Create center" className="auth-card">
                    <Form
                        style={{ marginBottom: '10px' }}
                        form={form}
                        layout="vertical"
                        onFinish={onFinish}
                        autoComplete="off"
                    >
                        <Form.Item
                            label="State"
                            name="state"
                            rules={[{ required: true, message: 'Please input your first name!' }]}
                        >
                            <Input />
                        </Form.Item>
                        <Form.Item
                            label="City"
                            name="city"
                            rules={[{ required: true, message: 'Please input your last name!' }]}
                        >
                            <Input />
                        </Form.Item>
                        <Form.Item
                            label="Name"
                            name="name"
                            rules={[{ required: true, message: 'Please input your email!' }]}
                        >
                            <Input />
                        </Form.Item>
                        <Form.Item
                            label="Address"
                            name="address"
                            rules={[{ required: true, message: 'Please input your email!' }]}
                        >
                            <Input />
                        </Form.Item>

                        <Form.Item>
                            <Button type="primary" htmlType="submit" block loading={isLoading}>
                                Create
                            </Button>
                        </Form.Item>
                    </Form>
                </Card>
            </div>
        </NavbarLayout>
    )
}

export default CenterPage;