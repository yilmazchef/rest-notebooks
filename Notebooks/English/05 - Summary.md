## 5\. Summary

In simple words, in the REST architectural style, data and functionality are considered resources and are accessed using **Uniform Resource Identifiers** (URIs).

The resources are acted upon by using a set of simple, well-defined operations. Also, the resources have to be decoupled from their representation so that clients can access the content in various formats, such as HTML, XML, plain text, PDF, JPEG, JSON, and others.

The clients and servers exchange representations of resources by using a standardized interface and protocol. Typically HTTP is the most used protocol, but REST does not mandate it.

Metadata about the resource is made available and used to control caching, detect transmission errors, negotiate the appropriate representation format, and perform authentication or access control.

And most importantly, every interaction with the server must be stateless.

All these principles help RESTful applications to be simple, lightweight, and fast.

References:

-   [REST APIs must be hypertext-driven][1]
-   [REST Arch Style][2]

[1]: https://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven
[2]: https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm


hello