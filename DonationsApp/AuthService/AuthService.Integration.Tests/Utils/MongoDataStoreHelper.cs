using System;
using System.Threading.Tasks;
using AuthService.DataStore;
using AuthService.DataStore.Mongo;

namespace NationalInstruments.NbExecService.Integration.Tests.Utils
{
    /// <summary>
    /// Helper class for tests that allows to perform data operations directy on database.
    /// </summary>
    class MongoDataStoreHelper
    {
        private static class SingletonCreator
        {
            internal static readonly MongoDataStoreHelper Instance = new MongoDataStoreHelper();
        }

        private readonly IDataProvider _dataProvider;

        private MongoDataStoreHelper()
        {
            _dataProvider = new MongoDataProvider(
                new MongoDataContext(FakeSettingsProvider.ConnectionString),
                FakeSettingsProvider.UserCollection);
        }

        public static MongoDataStoreHelper Instance
        {
            get { return SingletonCreator.Instance; }
        }
    }
}
