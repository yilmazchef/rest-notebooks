## 1\. Guiding Principles of REST

The six guiding principles or [constraints of the RESTful architecture][1] are:

### 1.1. Uniform Interface

By applying the [principle of generality][2] to the components interface, we can simplify the overall system architecture and improve the visibility of interactions.

Multiple architectural constraints help in obtaining a uniform interface and guiding the behavior of components.

The following four constraints can achieve a uniform REST interface:

-   **Identification of resources** – The interface must uniquely identify each resource involved in the interaction between the client and the server.
-   **Manipulation of resources through representations** – The resources should have uniform representations in the server response. API consumers should use these representations to modify the resources state in the server.
-   **Self-descriptive messages** – Each resource representation should carry enough information to describe how to process the message. It should also provide information of the additional actions that the client can perform on the resource.
-   **Hypermedia as the engine of application state** – The client should have only the initial URI of the application. The client application should dynamically drive all other resources and interactions with the use of hyperlinks.

### 1.2. Client-Server

The client-server design pattern enforces the **separation of concerns**, which helps the client and the server components evolve independently.

By separating the user interface concerns (client) from the data storage concerns (server), we improve the portability of the user interface across multiple platforms and improve scalability by simplifying the server components.

While the client and the server evolve, we have to make sure that the interface/contract between the client and the server does not break.

### 1.3. Stateless

[Statelessness][3] mandates that each request from the client to the server must contain all of the information necessary to understand and complete the request.

The server cannot take advantage of any previously stored context information on the server.

For this reason, the client application must entirely keep the session state.

### 1.4. Cacheable

The [cacheable constraint][4] requires that a response should implicitly or explicitly label itself as cacheable or non-cacheable.

If the response is cacheable, the client application gets the right to reuse the response data later for equivalent requests and a specified period.

### 1.5. Layered System

The layered system style allows an architecture to be composed of hierarchical layers by constraining component behavior.

For example, in a layered system, each component cannot see beyond the immediate layer they are interacting with.

### 1.6. Code on Demand (_Optional_)

REST also allows client functionality to extend by downloading and executing code in the form of applets or scripts.

The downloaded code simplifies clients by reducing the number of features required to be pre-implemented. Servers can provide part of features delivered to the client in the form of code, and the client only needs to execute the code.

[1]: https://restfulapi.net/rest-architectural-constraints/
[2]: https://www.d.umn.edu/~gshute/softeng/principles.html
[3]: https://restfulapi.net/statelessness/
[4]: https://restfulapi.net/caching/

