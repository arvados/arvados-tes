Task Execution Service for Arvados
==================================

This is an implementation of the `GA4GH Task
Execution
Service <https://github.com/ga4gh/task-execution-schemas>`__ for an `Arvados <https://github.com/curoverse/arvados>`__
backend.

Installation:

::

    pip install arvados-tes

Run the server:

::

    $ arvados-tes


GetServiceInfo
curl http://127.0.0.1:5000/ga4gh/tes/v1/service-info

ListTasks
curl http://127.0.0.1:5000/ga4gh/tes/v1/tasks

CreateTask
curl --data-binary @test.post -H "Content-Type: application/json" http://127.0.0.1:5000/ga4gh/tes/v1/tasks

GetTask
curl http://127.0.0.1:5000/ga4gh/tes/v1/tasks/{id}

CancelTask
