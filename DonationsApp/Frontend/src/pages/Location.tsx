import { Select } from "antd";
import Table, { ColumnsType } from "antd/es/table";
import { useEffect, useState } from "react";
import { useGetCenters, useGetCitiesByState, useGetStates } from "../state/index";
import { Center } from "~/types";

interface Props {
    center: Center,
    setCenter(value: Center | null): void,
}
const LocationContent: React.FC<Props> = ({ setCenter }) => {
    const [state, setState] = useState<string>("");
    const [city, setCity] = useState<string>("");

    const { data: states } = useGetStates();
    const { data: cities, refetch: refetchCity } = useGetCitiesByState(state);
    const { data: centers, refetch: refetchCenters } = useGetCenters(city, state);

    useEffect(() => {
        if (state) {
            refetchCity();
        }
    }, [state]);

    useEffect(() => {
        if (city) {
            refetchCenters();
        }
    }, [city]);

    const columns: ColumnsType<Center> = [
        {
            title: 'Name',
            dataIndex: 'name',
            render: (text: string) => <a>{text}</a>,
        },
        {
            title: 'State',
            dataIndex: 'state',
        },
        {
            title: 'City',
            dataIndex: 'city',
        },
        {
            title: 'Address',
            dataIndex: 'address',
        },
    ];

    // rowSelection object indicates the need for row selection
    const rowSelection = {
        onChange: (selectedRowKeys: React.Key[], selectedRow: Center[]) => {
            if (selectedRow) {
                setCenter(selectedRow[0] ?? null);
                console.log(`selectedRowKeys: ${selectedRowKeys}`, 'selectedRow: ', selectedRow)
            }
        },
    };

    const onChangeState = (value: string) => {
        setState(value);
    }

    const onChangeCity = (value: string) => {
        setCity(value);
    }


    return (
        <>
            <div>
                <Select
                    showSearch
                    style={{ width: 200 }}
                    placeholder="Choose State"
                    optionFilterProp="children"
                    options={states?.data.map((locationValue: string) => ({
                        value: locationValue,
                        label: locationValue
                    }))
                    }
                    onChange={onChangeState}
                />

                <Select
                    showSearch
                    style={{ width: 200, marginLeft: "20px" }}
                    placeholder="Choose City"
                    optionFilterProp="children"
                    options={cities?.data.map((locationValue: string) => ({
                        value: locationValue,
                        label: locationValue
                    }))}
                    onChange={onChangeCity}
                />
            </div>
            <div>
                {state && city && centers?.data.length && (
                    <Table
                        rowSelection={{
                            type: "radio",
                            ...rowSelection,
                        }}
                        columns={columns}
                        dataSource={centers.data.map((center: any, index: number) => ({
                            id: center.id,
                            key: index,
                            name: center.name,
                            state: center.state,
                            city: center.city,
                            address: center.address,
                        }))}
                    />
                )}
            </div>
        </>
    )
}


export default LocationContent;