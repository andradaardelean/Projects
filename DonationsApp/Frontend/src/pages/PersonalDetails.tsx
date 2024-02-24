import { Form, Input } from "antd";
import { useEffect, useState } from "react";

interface Props {
    personalDetails: any,
    setPersonalDetails(value: any | null): void,
}

const PersonalDetails: React.FC<Props> = ({setPersonalDetails}) => {

    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [address, setAddress] = useState('');
    const onChangeFN = (e: any) => {
        setFirstName(e.target.value);
    };

    const onChangeLN = (e: any) => {
        setLastName(e.target.value);
    };

    const onChangeAddress = (e: any) => {
        setAddress(e.target.value);
    };

    useEffect(() => {
        if(firstName && lastName && address){
            setPersonalDetails({firstName, lastName, address});
        }
    }, [firstName, lastName, address]);
    
    return (
        <div
            style={{ paddingBottom: "10px", border: "0px ridge", borderColor: "#ffabbd", marginLeft: "35%", width: "40%", padding: "20px" }}>
            <Form labelCol={{ span: 4 }} wrapperCol={{ span: 12 }}>
                <Form.Item label="First Name"
                    rules={[{ required: true, message: 'Please input your first name!' }]}
                >
                    <Input onChange={onChangeFN} />
                </Form.Item>
                <Form.Item label="Last Name"
                    rules={[{ required: true, message: 'Please input your last name!' }]}
                >
                    <Input onChange={onChangeLN}/>
                </Form.Item>
                <Form.Item label="Address"
                    rules={[{ required: true, message: 'Please input your address!' }]}
                >
                    <Input onChange={onChangeAddress}/>
                </Form.Item>
            </Form>
        </div>
    )
}

export default PersonalDetails;