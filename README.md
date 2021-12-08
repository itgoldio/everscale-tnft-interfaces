# TNFT Interfaces

Ссылка на описание технологии True-NFT - https://github.com/itgoldio/everscale-tnft

## Содержание
* [__Описание__](#description)
* [__Интерфейсы:__](#smart_contracts)
    * [Data Interfaces](#dataint)
      * [IRequiredInterfaces](#ireqint)
      * [IName](#idescription)
      * [IDescription](#idescription)
      * [ITags](#itags)
      * [IStoreIPFS](#istoreipfs)
      * [IMIMEType](#imimetype)
      * [ICollectable](#icollectable)
      * [IBurnByCreator](#iburnbycreator)
      * [IBurnByOwner](#iburnbyowner)
      * [ICustomInterfaces](#icustominterfaces)
    * [NftRoot Interfaces](#nftrootint)
      * [ICollectable](#rootcoll)
      * [ICustomInterfaces](#rootcustint)
      * [IRequiredInterfaces](#rootreqint)
      * [IStoreIPFS](#rootstoreipfs)
      * [IStoreOnChain](#rootstoreonchain)

<h1 id="description">Описание технологии интерфейсов</h1>

Проблема:

* <a href="https://github.com/itgoldio/everscale-tnft">True-NFT стандарт</a> слишком простой и требует доработки под нужный use-case.
* При добавлении нового функционала разработчики off-chain приложений должны искать интерфейсы для взаимодействия с новыми механиками.

Наше решение состоит из простых интерфейсов (модулей), у которых есть ID и abstract contract, который имплементирует методы интерфейса.
У каждого интерфейса есть уникальный идентификатор (ID), собранный по правилам:

* 1 - интерфейс getInterfaces
* от 2 до 4999 - стандартные интерфейсы (из этого репозитория)
* 41000 - интерфейс getCustomInterfaces, который содержит переменную - url кастомных интерфейсов.
* от 41001 до ∞ - кастомные интерфейсы, написанные разработчиками для своего продукта (которые можно найти по url кастомных интерфейсов) 
  
Если в контрактах используются какие-то интерфейсы (кастомные или из этого репозитория) - необходимо имплементировать абстрактный контракт RequiredInterfaces и в конструкторе
переменной _requiredInterfaces установить значения всех используемых интерфейсов:

```
 _requiredInterfaces = [RequiredInterfacesLib.ID, INameLib.ID ...];
```

Контракт должен имплементировать абстрактный контракт, не интерфейс:

```
    Yes: 
    contract Name is RequiredInterfaces, Name

    No: 
    contract Name is IRequiredInterfaces, IName
```

Каждый интерфейс должен содержать в себе такую структуру:

```
interface IName {
    function getName() external returns (string dataName);
}

library NameLib {
    int constant ID = 2;        
}

abstract contract Name is IName {

    string _dataName;

    function getName() public override returns (string dataName) {
        return _dataName;
    }   

}

```

Если вы имплементируете какой-то интерфейс - в конструкторе необходимо установить значения из их абстрактного контракта

```
contract Name is RequiredInterfaces, Name { 
    // Не забываем имплементировать интерфейс RequiredInterfaces
    constructor(
        ...
        string dataName
    ) {
        _dataName = dataName;
        _requiredInterfaces = [RequiredInterfacesLib.ID, NameLib.ID ...];
        // Не забываем устанавливать значение _requiredInterfaces
    }
}
```

<h1 id="smart_contracts">Интерфейсы</h1>

<h1 id="dataint">Data Interfaces</h1>

<h2 id="ireqint">IRequiredInterfaces</h2>

Возвращает массив ID всех использующихся интерфейсов в контракте
```
int[] _requiredInterfaces;

function getRequiredInterfaces() external returns(int[] requiredInterfaces);
function getRequiredInterfacesResponsible() external responsible returns(int[] requiredInterfaces);
```

<h2 id="iname">IName</h2>

Используется для добавления названия Nft в Data контракт
```
string _dataName;

function getName() external returns (string dataName);
function getNameResponsible() external responsible returns (string dataName);
```

<h2 id="idescription">IDescription</h2>

Используется для добавления описания Nft в Data контракт
```
string _dataDescription;

function getDescription() external returns (string dataDescription);
function getDescriptionResponsible() external responsible returns (string dataDescription);
```

<h2 id="itags">ITags</h2>

Используется для добавления тэгов Nft в Data контракт.
Например, в вашей коллекции есть разделение Nft по редкости: Common, Rare, Legendary
```
string[] _tags;

function getTags() external returns (string[] tags);
function getTagsResponsible() external responsible returns (string[] tags);
```

<h2 id="imimetype">IMIMEType</h2>

Используется для добавления mimetype данных(медиа) Nft в Data контракт. Подробнее о MIME type <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types">тут</a>
```
string _mimeType;

function getMIMEType() external returns (string mimeType);
function getMIMETypeResponsible() external responsible returns (string mimeType);
```

<h2 id="istoreipfs">IStoreIPFS</h2>

Используется для добавления url IPFS, где лежат данные Nft, если мы храним данные вне блокчейна.
```
string _dataUrl;

function getDataUrl() external returns(string dataUrl);
function getDataUrlResponsible() external responsible returns(string dataUrl);
```

<h2 id="icollectable">ICollectable</h2>

Используется для добавления параметров коллекции в Data контракт.
```
string _collectionName;
uint8 _editionNumber;
uint8 _editionAmount;

function getCollectionInfo() external returns(string collectionName, uint8 editionNumber, uint8 editionAmount); 
function getCollectionInfoResponsible() external responsible returns(string collectionName, uint8 editionNumber, uint8 editionAmount);
```

<h2 id="iburnbycreator">IBurnByCreator</h2>

Содержит метод burn, который может вызвать только создатель (NftRoot)
```
function burnByCreator() external;
```

<h2 id="iburnbyowner">IBurnByOwner</h2>

Содержит метод burn, который может вызвать только владелец, работает от internal messages
```
function burnByOwner() external;
```

<h2 id="icustominterfaces">ICustomInterfaces</h2>

Используется в случае, если вы написали свои интерфейсы. В параметр _customInterfacesUrl необходимо вписать url на репозиторий с интерфейсами. Кастомные интерфейсы должны содержать ID > 41000
```
string _customInterfacesUrl;

function getCustomInterfacesUrl() external returns (string url);
function getCustomInterfacesUrlResponsible() external responsible returns (string url);
```

<h1 id="nftrootint">NftRoot Interfaces</h1>

<h2 id="rootreqint">IRequiredInterfaces</h2>

Возвращает массив ID всех использующихся интерфейсов в контракте
```
int[] _requiredInterfaces;

function getRequiredInterfaces() external returns(int[] requiredInterfaces);
function getRequiredInterfacesResponsible() external responsible returns(int[] requiredInterfaces);
```


<h2 id="rootstoreipfs">IStoreIPFS</h2>

Используется для добавления url IPFS, где лежит иконка Nft коллекции, если мы храним ее вне блокчейна.
```
string _iconUrl;

function getIconUrl() external returns(string iconUrl); 
function getIconUrlResponsible() external responsible returns(string iconUrl);
```

<h2 id="rootstoreonchain">IStoreOnChain</h2>

Используется для добавления адреса аккаунта, где лежит иконка Nft коллекции, если мы храним ее в блокчейне.
```
address _iconAddr;

function getIconAddr() external returns(address iconAddr); 
function getIconAddrResponsible() external responsible returns(address iconAddr);
```

<h2 id="rootcoll">ICollectable</h2>

Используется для добавления параметров коллекции в NftRoot контракт.
```
string _collectionName;
string _collectionDescription;
uint8 _editionAmount;

function getCollectionInfo() external returns(string collectionName, string collectionDescription, uint8 editionAmount); 
function getCollectionInfoResponsible() external responsible returns(string collectionName, string collectionDescription, uint8 editionAmount);
```

<h2 id="rootcustint">ICustomInterfaces</h2>

Используется в случае, если вы написали свои интерфейсы. В параметр _customInterfacesUrl необходимо вписать url на репозиторий с интерфейсами. Кастомные интерфейсы должны содержать ID > 41000
```
string _customInterfacesUrl;

function getCustomInterfacesUrl() external returns (string url);
function getCustomInterfacesUrlResponsible() external responsible returns (string url);
```