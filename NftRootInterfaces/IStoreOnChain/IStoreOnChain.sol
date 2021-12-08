pragma ton-solidity = 0.47.0;

interface IStoreOnChain {
    function getIconAddr() external returns(address iconAddr); 
    function getIconAddrResponsible() external responsible returns(address iconAddr);
}

library StoreOnChainLib {
    int constant ID = 4;        
}

abstract contract StoreOnChain is IStoreOnChain{

    address _iconAddr;

    function getIconAddr() external override returns(address iconAddr) {
        return _iconAddr;
    }

    function getIconAddrResponsible() external override responsible returns(address iconAddr) {
        return {value: 0, flag: 64}(_iconAddr);
    }

} 