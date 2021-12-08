pragma ton-solidity = 0.47.0;

interface IBurnByOwner {
    function burnByOwner() external;
}

library BurnByOwnerLib {
    int constant ID = 9;        
}