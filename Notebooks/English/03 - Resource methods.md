## 3\. Resource Methods

Another important thing associated with REST is **resource methods**. These resource methods are used to perform the desired transition between two states of any resource.

A large number of people wrongly relate resource methods to [HTTP methods][1] (i.e., GET/PUT/POST/DELETE). Roy Fielding has never mentioned any recommendation around which method to be used in which condition. All he emphasizes is that it should be a **uniform interface**.

For example, if we decide that the application APIs will use HTTP POST for updating a resource – rather than most people recommend HTTP PUT – it’s all right. Still, the application interface will be RESTful.

Ideally, everything needed to transition the resource state shall be part of the resource representation – including all the supported methods and what form they will leave the representation.

> We should enter a REST API with no prior knowledge beyond the initial URI (a bookmark) and a set of standardized media types appropriate for the intended audience (i.e., expected to be understood by any client that might use the API).
> 
> From that point on, all application state transitions must be driven by the client selection of server-provided choices present in the received representations or implied by the user’s manipulation of those representations.
> 
> The transitions may be determined (or limited by) the client’s knowledge of media types and resource communication mechanisms, both of which may be improved on the fly (e.g., _code-on-demand_). \[Failure here implies that out-of-band information is driving interaction instead of hypertext.\]

[1]: https://restfulapi.net/http-methods/

