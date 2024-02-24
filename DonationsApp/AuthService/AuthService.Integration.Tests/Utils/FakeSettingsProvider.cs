using AuthService.WebApi.Settings;
using System;
using System.Globalization;

namespace NationalInstruments.NbExecService.Integration.Tests.Utils
{
    /// <summary>
    /// Class that fakes the Environment Variables for testing.
    /// </summary>
    public static class FakeSettingsProvider 
    {
        public static string BindingAddress => "http://localhost";

        public static int Port => 12500;

        public static string ConnectionString => "Data Source=E:\\Facultate\\Sem_4\\MPP\\Laboratoare\\Lab3\\mpp-proiect-csharp-Catalin-web\\Proiect\\Proiect\\Files\\exursii.db;version=3;new=False;datetimeformat=CurrentCulture;";

        public static string UserCollection => "users";
    }
}
