import { Form, InputNumber, Radio, RadioChangeEvent } from "antd"
import TextArea from "antd/es/input/TextArea";
import { useEffect, useState } from "react";

interface Props {
    recipient: any,
    setRecipient(value: any | null): void,
}
const Recipient: React.FC<Props> = ({ setRecipient }) => {

    //gender
    const [gender, setGender] = useState(0);
    const onChangeGender = (e: RadioChangeEvent) => {
        setGender(e.target.value);
    };


    //number
    const [age, setAge] = useState(0);
    const onChange = (value: number | null) => {
        if (value) setAge(value);
    };


    //donation
    const [donation, setDonation] = useState("");
    const onChangeDonation = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
        setDonation(e.target.value);
    };

    useEffect(() => {
        if (age && donation) {
            setRecipient({
                Gender: gender, 
                Age: age, 
                Donation: donation
            })
        }
    }, [gender, age, donation]);


    return (
        <div
            style={{ paddingBottom: "10px", border: "0px ridge", marginLeft: "35%", width: "40%", paddingTop: "30px", position: 'relative', top: '0' }}>
            <Form
                layout="horizontal"
                style={{ maxWidth: 600, }}
            >
                <Form.Item label="Gender" labelCol={{ span: 4 }}
                    wrapperCol={{ span: 8 }}>
                    <Radio.Group onChange={onChangeGender} value={gender}>
                        <Radio value={0}> Female </Radio>
                        <Radio value={1}> Male </Radio>
                    </Radio.Group>
                </Form.Item>
                <Form.Item label="Age" labelCol={{ span: 4 }}
                    wrapperCol={{ span: 3 }}>
                    <InputNumber value={age} onChange={onChange} min={1} max={18} />
                </Form.Item>
                <Form.Item label="Donation" labelCol={{ span: 4 }}
                    wrapperCol={{ span: 12 }}>
                    <TextArea onChange={onChangeDonation} rows={4} />
                </Form.Item>
            </Form>
        </div >
    )
}

export default Recipient;