pragma ton-solidity = 0.47.0;

interface IStoreIconIPFS {
    function getIconUrl() external returns(string iconUrl); 
    function getIconUrlResponsible() external responsible returns(string iconUrl);
}

library StoreIconIPFSLib {
    int constant ID = 3;        
}

abstract contract StoreIconIPFS is IStoreIconIPFS{

    string _iconUrl;

    function getIconUrl() external override returns(string iconUrl) {
        return _iconUrl;
    }

    function getIconUrlResponsible() external override responsible returns(string iconUrl) {
        return {value: 0, flag: 64}(_iconUrl);
    }

} 