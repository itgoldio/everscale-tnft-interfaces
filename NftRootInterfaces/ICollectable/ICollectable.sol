pragma ton-solidity = 0.47.0;

interface ICollectable {
    function getCollectionInfo() external returns(string collectionName, string collectionDescription, uint editionAmount); 
    function getCollectionInfoResponsible() external responsible returns(string collectionName, string collectionDescription, uint editionAmount);
}

library CollectableLib {
    int constant ID = 2;        
}

abstract contract Collectable is ICollectable{

    string _collectionName;
    string _collectionDescription;
    uint _editionAmount;

    function getCollectionInfo() external override returns(string collectionName, string collectionDescription, uint editionAmount) {
        return (_collectionName, _collectionDescription, _editionAmount);
    }

    function getCollectionInfoResponsible() external override responsible returns(string collectionName, string collectionDescription, uint editionAmount) {
        return {value: 0, flag: 64}(_collectionName, _collectionDescription, _editionAmount);
    }

} 
