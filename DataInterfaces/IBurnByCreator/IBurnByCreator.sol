pragma ton-solidity = 0.47.0;

interface IBurnByCreator {
    function burnByCreator() external;
}

library BurnByCreatorLib {
    int constant ID = 8;        
}
