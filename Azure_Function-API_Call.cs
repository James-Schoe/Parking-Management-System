// Inital Azure Function code: The Azure Function was triggered by a HTTP request from the Pico W. 
// This code lets calls the Graph API and write parking statuses into a SharePoint list. 
// The later version of this system encorperated a JSON payload & schema, but can't be displayed due to company policy. 
// While AI helped me write this code, I wrote and understood every line of this code at the time of creating the script, (hence logical comments). 

using System.Net;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;
using Microsoft.Graph;
using Microsoft.Graph.Models;
using Azure.Identity;
using Azure.Core;


namespace Parking.Management;

public class API_Test // Creating a class within Parking.Management 
{
    private readonly ILogger<API_Test> _logger; // Running the class API_Test through the Ilogger interface and storing the output in _logger

    public API_Test(ILogger<API_Test> logger) // Constructor 'API_Test' is recieving the value of 'logger'
    {
        _logger = logger; // Value of 'logger' now equals value of _logger 
    }
    
    // Function HTTP Trigger:
    [Function("API_Test")] // Function name = API_Test 
    public async Task<HttpResponseData> Run(
        [HttpTrigger(AuthorizationLevel.Function, "get","post")] HttpRequestData req)
    {

    // API endpoint code: 
        _logger.LogInformation("HTTP trigger processed"); 
        
        var credential = new ManagedIdentityCredential(); 
        var scopes = new[] { "https://graph.microsoft.com/.default" };

       // _logger.LogInformation("Retrieving token");

       // await credential.GetTokenAsync(new TokenRequestContext(scopes)); // Testing MI token retrieval

        _logger.LogInformation("Requesting Token");
        var token = await credential.GetTokenAsync(new TokenRequestContext(scopes));        
        _logger.LogInformation("Token Retrieved");

        var graphServiceClient = new GraphServiceClient(credential, scopes);  

        var siteId = "Censored_SiteID"; //Site address, SiteId and WebId
        var listId = "Censored_WebID";

        await graphServiceClient.Sites[siteId].Lists[listId].Items.PostAsync(
            new ListItem {
                Fields = new FieldValueSet {
                    AdditionalData = new Dictionary<string, object> {
                        {"Title", "1"} // Although column label is 'BinaryValue', it's internal name is 'Title'.
                    }
                }
            });

        var response = req.CreateResponse(HttpStatusCode.OK);
        await response.WriteStringAsync("Complete"); // Displaying "Complete" in the response body of the HTTP response
        _logger.LogInformation("List item created.");
        return response;     

    }
}
