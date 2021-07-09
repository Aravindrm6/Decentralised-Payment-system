pragma solidity >=0.4.22 <0.9.0;
pragma experimental ABIEncoderV2;
contract MyContract{
    struct vehicle{
        uint vid;
        address vehicle;
        uint price_per_km;
        mapping(string=>uint)d;
        uint time;
        uint price;
    }
    struct status{
        string [] Location;
        uint [] time;
        uint []price;
    }
    uint i;
    constructor()public{
        i=0;
    }
mapping(address => vehicle) public vehicleMapping;
mapping(address => status) statusMapping;
mapping(address => bool) public reg_vehicle;
function getVehicle() public view returns(uint){
    return vehicleMapping[msg.sender].vid;
}
function getindex() public view returns(uint){
    return i;
}
function getStatusLocation() public view returns(string[] memory){
    return statusMapping[msg.sender].Location;
}
function getStatusTime() public view returns(uint[] memory){
    return statusMapping[msg.sender].time;
}
function getStatusPrice() public view returns(uint[] memory){
    return statusMapping[msg.sender].price;
}
function getDistance(string memory e) public view returns(uint){
    return vehicleMapping[msg.sender].d[e];
}
function regVehicle(uint price) public returns(string memory){
    if(reg_vehicle[msg.sender]==true)
        return "Multiple registration Not Allowed";
    reg_vehicle[msg.sender]=true;
    i++;
    vehicleMapping[msg.sender].vid=i;
    vehicleMapping[msg.sender].price_per_km=price;
    vehicleMapping[msg.sender].time=block.timestamp;
    vehicleMapping[msg.sender].price=0;
    vehicleMapping[msg.sender].d['25,51']=12;
    vehicleMapping[msg.sender].d['22,53']=34;
    vehicleMapping[msg.sender].d['23,62']=41;
    vehicleMapping[msg.sender].d['26,71']=29;
    vehicleMapping[msg.sender].d['24,33']=33;
    return "Vehicle Registered Successfully";
}
function updateLocation(string memory _Location) public returns(string memory){
    statusMapping[msg.sender].Location.push(_Location);
    statusMapping[msg.sender].time.push(block.timestamp);
    statusMapping[msg.sender].price.push(vehicleMapping[msg.sender].price);
    return "Location detail updated";
    
}
function getPrice() public view returns (uint){
    return vehicleMapping[msg.sender].price;
}
function generateBill(uint distance)public returns(string memory){
    vehicleMapping[msg.sender].price=distance*vehicleMapping[msg.sender].price_per_km;
    vehicleMapping[msg.sender].time=block.timestamp;
    return "Bill added";
}
}