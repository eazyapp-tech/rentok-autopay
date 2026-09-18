<!-- Captured 18 Sep 2026 from Cashfree's Subscriptions documentation (https://www.cashfree.com/docs/). Cashfree's live page is the authority. -->

> ## Documentation Index
> Fetch the complete documentation index at: https://www.cashfree.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a Plan

> A plan allows your customer to identify the features you offer along with your pricing. You can create plans as per the pricing you support for your services. For each plan, you can set a pre-decided frequency and amount with which they’ll be charged.
Example: Netflix Plans : Premium, Basic, Standard, Mobile. Each plan differs and caters for a particular set of audiences.



## OpenAPI

````yaml openapi/payments/v2026-01-01.yaml post /plans
openapi: 3.0.0
info:
  version: '2026-01-01'
  title: Cashfree Payment Gateway APIs
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0.html
  contact:
    email: developers@cashfree.com
    name: API Support
    url: https://discord.com/invite/QdZkNSxXsB
  description: >-
    Cashfree's Payment Gateway APIs provide developers with a streamlined
    pathway to integrate advanced payment processing capabilities into their
    applications, platforms and websites.
servers:
  - url: https://sandbox.cashfree.com/pg
    description: Sandbox server.
  - url: https://api.cashfree.com/pg
    description: Production server.
security: []
tags:
  - name: Orders
    description: Collection of APIs to handle orders.
  - name: Payments
    description: Collection of APIs to handle payments.
  - name: Refunds
    description: Collection of APIs to handle refunds.
  - name: Settlements
    description: Collection of APIs to handle settlements.
  - name: Payment Links
    description: Collection of APIs to handle payment links.
  - name: Token Vault
    description: >-
      Collection of APIs to use Cashfree's token Vault. This helps you save
      cards and tokenize them in a PCI complaint manner. We support creation of
      network tokens which can be used across acquiring banks.
  - name: softPOS
    description: Collection of APIs to manage softPOS' agent and order.
  - name: Offers
    description: Collection of APIs to handle offers.
  - name: Eligibility
    description: >-
      Collection of APIs to check eligibile entities - payment methods, offer,
      affordibility.
  - name: Settlement Reconciliation
    description: Collection of APIs to handle settlements.
  - name: PG Reconciliation
    description: Collection of APIs to handle reconciliation.
  - name: Customers
    description: Collection of APIs to handle customers.
  - name: Easy-Split
    description: Collection of APIs to handle Easy-Split.
  - name: Simulation
    description: Collection of APIs to handle simulation.
  - name: Disputes
    description: Collection of APIs to handle disputes.
  - name: Utilities
    description: Collection of APIs for utility requirement.
  - name: Downtimes
    description: Collection of APIs for managing downtimes.
externalDocs:
  url: https://api.cashfree.com/pg
  description: This url will have the information of all the APIs.
paths:
  /plans:
    post:
      tags:
        - Subscription
      summary: Create a Plan
      description: >-
        A plan allows your customer to identify the features you offer along
        with your pricing. You can create plans as per the pricing you support
        for your services. For each plan, you can set a pre-decided frequency
        and amount with which they’ll be charged.

        Example: Netflix Plans : Premium, Basic, Standard, Mobile. Each plan
        differs and caters for a particular set of audiences.
      operationId: SubsCreatePlan
      parameters:
        - $ref: '#/components/parameters/apiVersionHeader'
        - $ref: '#/components/parameters/xRequestIDHeader'
        - $ref: '#/components/parameters/xIdempotencyKeyHeader'
      requestBody:
        $ref: '#/components/requestBodies/CreatePlanRequest'
      responses:
        '200':
          description: Success response for creating a plan.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PlanEntity'
          headers:
            x-api-version:
              $ref: '#/components/headers/x-api-version'
            x-ratelimit-limit:
              $ref: '#/components/headers/x-ratelimit-limit'
            x-ratelimit-remaining:
              $ref: '#/components/headers/x-ratelimit-remaining'
            x-ratelimit-retry:
              $ref: '#/components/headers/x-ratelimit-retry'
            x-ratelimit-type:
              $ref: '#/components/headers/x-ratelimit-type'
            x-request-id:
              $ref: '#/components/headers/x-request-id'
            x-idempotency-key:
              $ref: '#/components/headers/x-idempotency-key'
            x-idempotency-replayed:
              $ref: '#/components/headers/x-idempotency-replayed'
        '400':
          $ref: '#/components/responses/Response400'
        '401':
          $ref: '#/components/responses/Response401'
        '404':
          $ref: '#/components/responses/Response404'
        '422':
          $ref: '#/components/responses/Response422'
        '429':
          $ref: '#/components/responses/Response429'
        '500':
          $ref: '#/components/responses/Response500'
      deprecated: false
      security:
        - XClientID: []
          XClientSecret: []
        - XClientID: []
          XPartnerAPIKey: []
        - XClientID: []
          XClientSignatureHeader: []
        - XPartnerMerchantID: []
          XPartnerAPIKey: []
components:
  parameters:
    apiVersionHeader:
      in: header
      name: x-api-version
      required: true
      description: API version to be used. Format is in YYYY-MM-DD.
      schema:
        type: string
        description: API version to be used.
        default: '2026-01-01'
      example: '2026-01-01'
      x-ignore: true
    xRequestIDHeader:
      in: header
      name: x-request-id
      description: >-
        Request ID for the API call. Can be used to resolve tech issues.
        Communicate this in your tech related queries to Cashfree.
      required: false
      schema:
        type: string
      example: 4dfb9780-46fe-11ee-be56-0242ac120002
    xIdempotencyKeyHeader:
      in: header
      name: x-idempotency-key
      required: false
      description: >
        An idempotency key is a unique identifier you include with your API
        call.

        If the request fails or times out, you can safely retry it using the
        same key to avoid duplicate actions.
      schema:
        type: string
        format: UUID
      example: 47bf8872-46fe-11ee-be56-0242ac120002
  requestBodies:
    CreatePlanRequest:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/CreatePlanRequest'
  schemas:
    PlanEntity:
      title: PlanEntity
      type: object
      example:
        plan_currency: INR
        plan_id: 144436-03471-JD_TEST
        plan_interval_type: WEEK
        plan_intervals: 1
        plan_max_amount: 1
        plan_max_cycles: 4
        plan_name: abscede
        plan_note: lsdkdn
        plan_recurring_amount: 1
        plan_status: ACTIVE
        plan_type: PERIODIC
      properties:
        plan_currency:
          type: string
          description: Currency for the plan.
        plan_id:
          type: string
          description: Plan ID provided by merchant.
        plan_interval_type:
          type: string
          description: Interval type for the plan.
        plan_intervals:
          type: integer
          description: Number of intervals for the plan.
        plan_max_amount:
          type: number
          format: float64
          description: Maximum amount for the plan.
        plan_max_cycles:
          type: integer
          description: Maximum number of payment cycles for the plan.
        plan_name:
          type: string
          description: Name of the plan.
        plan_note:
          type: string
          description: Note for the plan.
        plan_recurring_amount:
          type: number
          format: float64
          description: Recurring amount for the plan.
        plan_status:
          type: string
          description: Status of the plan.
        plan_type:
          type: string
          description: Type of the plan.
    CreatePlanRequest:
      title: CreatePlanRequest
      description: Request parameters to create a new plan.
      example:
        plan_id: plan_12345
        plan_name: Plan 12345
        plan_type: PERIODIC
        plan_currency: INR
        plan_recurring_amount: 10
        plan_max_amount: 100
        plan_max_cycles: 10
        plan_intervals: 2
        plan_interval_type: WEEK
        plan_note: Test Plan
      properties:
        plan_id:
          type: string
          description: >-
            Unique ID to identify the plan. Only alpha-numerics, dot, hyphen and
            underscore allowed.
          minLength: 1
          maxLength: 40
        plan_name:
          type: string
          description: Name of the plan.
          minLength: 1
          maxLength: 40
        plan_type:
          type: string
          description: Type of the plan. Possible values - PERIODIC, ON_DEMAND.
        plan_currency:
          type: string
          description: >-
            Currency of the plan. For plans in non-INR currency, please refer to
            [supported
            currencies](https://www.cashfree.com/docs/payments/international-payments/ipg/currencies-supported#full-currency-list).
        plan_recurring_amount:
          type: number
          format: float64
          description: Recurring amount for the plan. Required for PERIODIC plan_type.
        plan_max_amount:
          type: number
          format: float64
          description: Maximum amount for the plan.
        plan_max_cycles:
          type: integer
          description: Maximum number of payment cycles for the plan.
        plan_intervals:
          type: integer
          description: >-
            Number of billing cycles between charges. For instance, if set to 2
            and the interval type is 'week', the service will be billed every 2
            weeks. Similarly, if set to 3 and the interval type is 'month', the
            service will be billed every 3 months. Required for PERIODIC
            plan_type.
        plan_interval_type:
          type: string
          description: >-
            Interval type for the plan. Possible values - DAY, WEEK, MONTH,
            YEAR.
        plan_note:
          type: string
          description: Note for the plan.
      required:
        - plan_id
        - plan_name
        - plan_type
        - plan_max_amount
    BadRequestError:
      title: BadRequestError
      description: Invalid request received from client.
      example:
        message: bad URL, please check API documentation
        help: >-
          Check latest errors and resolution from Merchant Dashboard API logs:
          https://bit.ly/4glEd0W Help Document: https://bit.ly/4eeZYO9
        code: request_failed
        type: invalid_request_error
      type: object
      properties:
        message:
          type: string
        code:
          type: string
        help:
          type: string
        type:
          type: string
          enum:
            - invalid_request_error
    AuthenticationError:
      title: AuthenticationError
      description: Error if api keys are wrong.
      example:
        message: authentication Failed
        code: request_failed
        type: authentication_error
      type: object
      properties:
        message:
          type: string
        code:
          type: string
        type:
          type: string
          description: authentication_error.
    ApiError404:
      title: ApiError404
      description: Error when resource requested is not found.
      example:
        message: something is not found
        help: >-
          Check latest errors and resolution from Merchant Dashboard API logs:
          https://bit.ly/4glEd0W Help Document: https://bit.ly/4eeZYO9
        code: something_not_found
        type: invalid_request_error
      type: object
      properties:
        message:
          type: string
        code:
          type: string
        help:
          type: string
        type:
          type: string
          enum:
            - invalid_request_error
          description: invalid_request_error.
    IdempotencyError:
      title: IdempotencyError
      description: >-
        Error when idempotency fails. Different request body with the same
        idempotent key.
      example:
        message: something is not found
        help: >-
          Check latest errors and resolution from Merchant Dashboard API logs:
          https://bit.ly/4glEd0W Help Document: https://bit.ly/4eeZYO9
        code: request_invalid
        type: idempotency_error
      type: object
      properties:
        message:
          type: string
        help:
          type: string
        code:
          type: string
        type:
          type: string
          enum:
            - idempotency_error
          description: idempotency_error.
    RateLimitError:
      title: RateLimitError
      description: Error when rate limit is breached for your api.
      example:
        message: Too many requests from IP. Check headers
        code: request_failed
        type: rate_limit_error
      type: object
      properties:
        message:
          type: string
        code:
          type: string
        type:
          type: string
          enum:
            - rate_limit_error
          description: rate_limit_error.
    ApiError:
      title: ApiError
      description: Error at Cashfree's server.
      example:
        message: internal Server Error
        help: >-
          Check latest errors and resolution from Merchant Dashboard API logs:
          https://bit.ly/4glEd0W Help Document: https://bit.ly/4eeZYO9
        code: internal_error
        type: api_error
      type: object
      properties:
        message:
          type: string
        code:
          type: string
        help:
          type: string
        type:
          type: string
          enum:
            - api_error
          description: api_error.
  headers:
    x-api-version:
      schema:
        type: string
        format: YYYY-MM-DD
        enum:
          - '2026-01-01'
      description: >-
        This header has the version of the API. The current version is
        `2026-01-01`.
    x-ratelimit-limit:
      schema:
        type: integer
      example: 200
      description: Ratelimit set for your account for this API per minute.
    x-ratelimit-remaining:
      schema:
        type: integer
      example: 2
      description: >-
        Rate limit remaning for your account for this API in the next minute.
        Uses sliding window.
    x-ratelimit-retry:
      schema:
        type: integer
      example: 4
      description: |
        Contains number of seconds to wait if rate limit is breached
        - Is 0 if withing the limit
        - Is between 1 and 59 if breached
    x-ratelimit-type:
      schema:
        type: string
        enum:
          - app_id
          - ip
      example: ip
      description: >
        either ip or app_id

        - `ip` if making a call from the browser. True for api where you don't
        need `x-client-id` and `x-client-secret`

        - `app_id` for authenticated api calls i.e using `x-client-id` and
        `x-client-secret`
    x-request-id:
      schema:
        type: string
      example: some-req-id
      description: >-
        Request id for your api call. Is blank or null if no `x-request-id` is
        sent during the request.
    x-idempotency-key:
      schema:
        type: string
      example: some-idem-id
      description: >-
        An idempotency key is a unique identifier you include with your API
        call. If the request fails or times out, you can safely retry it using
        the same key to avoid duplicate actions.
    x-idempotency-replayed:
      schema:
        type: string
        format: boolean
      example: 'true'
      description: |-
        In conjunction with `x-idempotency-key` this means
        - `true` if the response was replayed
        - `false` if the response has not been replayed.
  responses:
    Response400:
      description: Bad request error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/BadRequestError'
      headers:
        x-api-version:
          $ref: '#/components/headers/x-api-version'
        x-ratelimit-limit:
          $ref: '#/components/headers/x-ratelimit-limit'
        x-ratelimit-remaining:
          $ref: '#/components/headers/x-ratelimit-remaining'
        x-ratelimit-retry:
          $ref: '#/components/headers/x-ratelimit-retry'
        x-ratelimit-type:
          $ref: '#/components/headers/x-ratelimit-type'
        x-request-id:
          $ref: '#/components/headers/x-request-id'
        x-idempotency-key:
          $ref: '#/components/headers/x-idempotency-key'
        x-idempotency-replayed:
          $ref: '#/components/headers/x-idempotency-replayed'
    Response401:
      description: Authentication Error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/AuthenticationError'
      headers:
        x-api-version:
          $ref: '#/components/headers/x-api-version'
        x-ratelimit-limit:
          $ref: '#/components/headers/x-ratelimit-limit'
        x-ratelimit-remaining:
          $ref: '#/components/headers/x-ratelimit-remaining'
        x-ratelimit-retry:
          $ref: '#/components/headers/x-ratelimit-retry'
        x-ratelimit-type:
          $ref: '#/components/headers/x-ratelimit-type'
        x-request-id:
          $ref: '#/components/headers/x-request-id'
        x-idempotency-key:
          $ref: '#/components/headers/x-idempotency-key'
        x-idempotency-replayed:
          $ref: '#/components/headers/x-idempotency-replayed'
    Response404:
      description: Resource Not found.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError404'
      headers:
        x-api-version:
          $ref: '#/components/headers/x-api-version'
        x-ratelimit-limit:
          $ref: '#/components/headers/x-ratelimit-limit'
        x-ratelimit-remaining:
          $ref: '#/components/headers/x-ratelimit-remaining'
        x-ratelimit-retry:
          $ref: '#/components/headers/x-ratelimit-retry'
        x-ratelimit-type:
          $ref: '#/components/headers/x-ratelimit-type'
        x-request-id:
          $ref: '#/components/headers/x-request-id'
        x-idempotency-key:
          $ref: '#/components/headers/x-idempotency-key'
        x-idempotency-replayed:
          $ref: '#/components/headers/x-idempotency-replayed'
    Response422:
      description: Idempotency error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/IdempotencyError'
      headers:
        x-api-version:
          $ref: '#/components/headers/x-api-version'
        x-ratelimit-limit:
          $ref: '#/components/headers/x-ratelimit-limit'
        x-ratelimit-remaining:
          $ref: '#/components/headers/x-ratelimit-remaining'
        x-ratelimit-retry:
          $ref: '#/components/headers/x-ratelimit-retry'
        x-ratelimit-type:
          $ref: '#/components/headers/x-ratelimit-type'
        x-request-id:
          $ref: '#/components/headers/x-request-id'
        x-idempotency-key:
          $ref: '#/components/headers/x-idempotency-key'
        x-idempotency-replayed:
          $ref: '#/components/headers/x-idempotency-replayed'
    Response429:
      description: Rate Limit Error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/RateLimitError'
      headers:
        x-api-version:
          $ref: '#/components/headers/x-api-version'
        x-ratelimit-limit:
          $ref: '#/components/headers/x-ratelimit-limit'
        x-ratelimit-remaining:
          $ref: '#/components/headers/x-ratelimit-remaining'
        x-ratelimit-retry:
          $ref: '#/components/headers/x-ratelimit-retry'
        x-ratelimit-type:
          $ref: '#/components/headers/x-ratelimit-type'
        x-request-id:
          $ref: '#/components/headers/x-request-id'
        x-idempotency-key:
          $ref: '#/components/headers/x-idempotency-key'
        x-idempotency-replayed:
          $ref: '#/components/headers/x-idempotency-replayed'
    Response500:
      description: API related Error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
      headers:
        x-api-version:
          $ref: '#/components/headers/x-api-version'
        x-ratelimit-limit:
          $ref: '#/components/headers/x-ratelimit-limit'
        x-ratelimit-remaining:
          $ref: '#/components/headers/x-ratelimit-remaining'
        x-ratelimit-retry:
          $ref: '#/components/headers/x-ratelimit-retry'
        x-ratelimit-type:
          $ref: '#/components/headers/x-ratelimit-type'
        x-request-id:
          $ref: '#/components/headers/x-request-id'
        x-idempotency-key:
          $ref: '#/components/headers/x-idempotency-key'
        x-idempotency-replayed:
          $ref: '#/components/headers/x-idempotency-replayed'
  securitySchemes:
    XClientID:
      type: apiKey
      in: header
      name: x-client-id
      description: >-
        Client app ID. You can find your app id in the [Merchant
        Dashboard](https://merchant.cashfree.com/auth/login/pg/developers/api-keys?env=prod).
    XClientSecret:
      type: apiKey
      in: header
      name: x-client-secret
      description: >-
        Client secret key. You can find your secret key in the [Merchant
        Dashboard](https://merchant.cashfree.com/auth/login/pg/developers/api-keys?env=prod).
    XPartnerAPIKey:
      type: apiKey
      in: header
      name: x-partner-apikey
      description: >-
        If you are partner and you are making an api call on behalf of a
        merchant.
    XClientSignatureHeader:
      type: apiKey
      in: header
      name: x-client-signature
      description: >-
        Use this if you do not want to pass the secret key and instead want to
        use signature.
    XPartnerMerchantID:
      type: apiKey
      in: header
      name: x-partner-merchantid
      description: >-
        If you are partner use this to specify the merchant ID if you don't have
        the merchant client app ID.

````