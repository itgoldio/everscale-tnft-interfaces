import tonos_ts4.ts4 as ts4

eq = ts4.eq

ts4.init('./', verbose = True)
VENDORING_PATH='../../../vendoring/'

#deploy
keypair = ts4.make_keypair()
setcodemultisig = ts4.BaseContract(VENDORING_PATH + 'setcodemultisig/SetcodeMultisigWallet', ctor_params = {'owners': [keypair[1]], 'reqConfirms': 1}, keypair = keypair)

codeIndex = ts4.load_code_cell(VENDORING_PATH + 'compiled/Index.tvc')
codeData = ts4.load_code_cell(VENDORING_PATH + 'compiled/Data.tvc')

print (keypair[1])

nftRoot = ts4.BaseContract('compiled/NftRoot', ctor_params = {'codeIndex': codeIndex, 'codeData': codeData, 'ownerPubkey': keypair[1]}, keypair = keypair)

ts4.dispatch_messages()

#id
IRequiredInterfaces = 1
ReqInterfaces = [IRequiredInterfaces]

answReqInterfaces = nftRoot.call_getter('getRequiredInterfaces')

assert eq(answReqInterfaces, ReqInterfaces)