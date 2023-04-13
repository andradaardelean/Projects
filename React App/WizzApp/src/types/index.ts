export interface User{
    id: string,
    fName:string,
    lName:string,
    email: string,
    password: string
}

export interface Flight{
    id: string,
    departure: string,
    destination: string,
    dateTime: Date,
    noSeats: number,
    return: boolean
}

export interface Passenger{
    id: string,
    fname: string,
    lname: string,
    dateOfBirth: Date,
    sex: string,
}

export interface Ticket{
    id:string,
    flight: Flight[],
    user: User,
    passengers?: Passenger[]
}