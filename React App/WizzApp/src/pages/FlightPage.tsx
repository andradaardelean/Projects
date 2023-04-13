import { useLocation } from "react-router-dom"
import { Flight } from "~/types";
import { queryToObject } from "~/utils/utils";


const flights: Flight[] = [
    {
        id: "1",
        departure: "cluj",
        destination: "oradea",
        dateTime: new Date(),
        noSeats: 80,
        return: true
    },
    {
        id: "2",
        departure: "cluj",
        destination: "oradea",
        dateTime: new Date(),
        noSeats: 100,
        return: false
    },
    {
        
        id: "3",
        departure: "oradea",
        destination: "cluj",
        dateTime: new Date(),
        noSeats: 150,
        return: false
    }
]

const FlightPage = () => {
    const { search } = useLocation();

   const data = queryToObject(search);
   
    return (
        <div>{data['departure']}</div>
    )
}

export default FlightPage