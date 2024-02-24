import { Button, message, Steps, theme } from "antd";
import { useState } from "react";
import NavbarLayout from "../layouts";
import 'index.css';
import LocationContent from "./Location";
import Recipient from "./Recipient";
import PersonalDetails from "./PersonalDetails";
import { useAddDonation } from "../state/index";
import { useNavigate } from "react-router";

const DonationPage = () => {
    const [center, setCenter] = useState<any | null>(null);
    const [recipient, setRecipient] = useState<any | null>(null);
    const [personalDetails, setPersonalDetails] = useState<any | null>(null);

    const [isLoading, setIsLoading] = useState<any>(false);

    const { mutate: donate } = useAddDonation(); //POST, PUT, DELETE

    const navigate = useNavigate();

    const handleAddDonation = () => {
        setIsLoading(true);
        if (center && recipient && personalDetails) {
            const data = {
                CenterId: center.id,
                ChildGroup: {
                    Age: recipient.Age,
                    Sex: recipient.Gender
                },
                GiftDescription: recipient.Donation,
                Donator: {
                    FirstName: personalDetails.firstName,
                    LastName: personalDetails.lastName,
                    HomeAddress: personalDetails.address,
                }
            };
            donate(data, {
                onSuccess: () => {
                    message.success("Donation added successfully");
                    setIsLoading(false);
                    setTimeout(() => {
                    navigate("/home");
                    }, 500);
                }
            });
        }
    };

    const steps = [
        {
            title: 'Choose Location',
            content: <LocationContent center={center} setCenter={setCenter} />,
        },
        {
            title: 'Recipient',
            content: <Recipient recipient={recipient} setRecipient={setRecipient} />,
        },
        {
            title: 'Personal Details',
            content: <PersonalDetails personalDetails={personalDetails} setPersonalDetails={setPersonalDetails} />,
        },
    ];

    const { token } = theme.useToken();
    const [current, setCurrent] = useState(0);

    const next = () => {
        setCurrent(current + 1);
    };

    const prev = () => {
        setCurrent(current - 1);
    };

    const items = steps.map((item) => ({ key: item.title, title: item.title }));

    const contentStyle: React.CSSProperties = {
        lineHeight: '200px',
        textAlign: 'center',
        color: token.colorTextTertiary,
        backgroundColor: token.colorFillAlter,
        borderRadius: token.borderRadiusLG,
        border: `1px dashed ${token.colorBorder}`,
        marginTop: 16,

    };

    return (
        <NavbarLayout tab={"2"}>
            <Steps current={current} items={items} style={{ padding: '20px', color: "black" }} />
            <div style={contentStyle}>{steps[current]?.content}</div>
            <div style={{ marginTop: 24, float: "right", marginRight: 50 }}>
                {current > 0 && (
                    <Button style={{ margin: '0 8px' }} onClick={() => prev()}>
                        Previous
                    </Button>
                )}
                {current < steps.length - 1 && (
                    <Button type="primary" onClick={() => next()} disabled={current === 1 && (recipient?.Gender == 0 || recipient?.Gender === 1) && !recipient?.Age && !recipient?.Donation}>
                        Next
                    </Button>
                )}
                {current === steps.length - 1 && (
                    <Button type="primary" onClick={handleAddDonation} loading={isLoading}>
                        Make donation
                    </Button>
                )}

            </div>
        </NavbarLayout>
    );
};

export default DonationPage;
