import { Button, Checkbox, DatePicker, Form, Select, message } from 'antd';
import { CheckboxChangeEvent } from 'antd/es/checkbox';
import { useState } from 'react';
import { useNavigate } from 'react-router';
import { objectToQuery } from '~/utils/utils';
import NumericInput from './NumberInput';

const { RangePicker } = DatePicker;

const SearchForm = () => {
  const [form] = Form.useForm();
  const options = ['cluj', 'oradea', 'satu mare'];
  const [noOfPassangers, setNoOfPassangers] = useState<string>('0');

  const navigate = useNavigate();

  const [checked, setChecked] = useState(true);

  const onChange = (e: CheckboxChangeEvent) => {
    setChecked(e.target.checked);
  };

  const validateFiels = (values: any) => {
    if (!values.departure) {
      message.error('Please select departure');
      return;
    }
    if (!values.destination) {
      message.error('Please select destination');
      return;
    }
    if (!values.date) {
      message.error('Please select date');
      return;
    }
    if (noOfPassangers === '0') {
      message.error('Please select number of passengers');
      return;
    }
    return true;
  };

  const handleSubmit = () => {
    const values = form.getFieldsValue();
    if (!validateFiels(values)) {
      return;
    }
    const url = `/flights${objectToQuery(values)}`;
    navigate(url);
  };

  return (
    <div style={{ backgroundColor: '#FFE2FB' }}>
      <div
        style={{
          paddingBottom: '10px',
          border: '0px ridge',
          borderColor: '#ffabbd',
          borderRadius: '5px',
          margin: 'auto',
          width: '40%',
          paddingTop: '20px'
        }}
      >
        <h1
          style={{
            color: '#FF9DF0 ',
            font: 'montserrat',
            textShadow: '2px 2px 4px #000000',
            position: 'relative',
            left: '20%'
          }}
        >
          Search flights
        </h1>
        <Form
          form={form}
          labelCol={{ span: 4 }}
          wrapperCol={{ span: 12 }}
          layout="horizontal"
          style={{ maxWidth: 600 }}
        >
          <Form.Item
            name="departure"
            style={{ position: 'relative', left: '20%' }}
          >
            <Select placeholder="LEAVING FROM">
              {options.map((o) => {
                return <Select.Option value={o}>{o}</Select.Option>;
              })}
            </Select>
          </Form.Item>
          <Form.Item
            name="destination"
            style={{ position: 'relative', left: '20%' }}
          >
            <Select placeholder="GOING TO">
              {options.map((o) => {
                return <Select.Option value={o}>{o}</Select.Option>;
              })}
            </Select>
          </Form.Item>
          <Form.Item name="oneWay">
            <p style={{ margin: '0 auto', position: 'relative', left: '41%' }}>
              <Checkbox checked={checked} onChange={onChange}>
                One-way
              </Checkbox>
            </p>
          </Form.Item>
          <Form.Item name="date" style={{ position: 'relative', left: '20%' }}>
            {checked ? <DatePicker /> : <RangePicker />}
          </Form.Item>
          <Form.Item
            name="passengers"
            style={{ position: 'relative', left: '20%' }}
          >
            <NumericInput
              style={{ width: 120 }}
              value={noOfPassangers}
              onChange={setNoOfPassangers}
            />
          </Form.Item>
          <Form.Item style={{ position: 'relative', left: '58%' }}>
            <Button
              onClick={handleSubmit}
              style={{ position: 'absolute', top: '50%' }}
            >
              Search
            </Button>
          </Form.Item>
        </Form>
      </div>
    </div>
  );
};

export default SearchForm;
