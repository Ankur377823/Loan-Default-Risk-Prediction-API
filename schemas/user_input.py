from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Annotated, Literal
from config.validators import ALLOWED_PURPOSES, HOME_OWNERSHIP, EMP_LENGTH_VALUES


class LoanApplication(BaseModel):

    # Loan Features

    loan_amnt: Annotated[
        float,
        Field(
            gt=0,
            description="Total loan amount requested by the borrower (log-transformed in dataset).",
            example=9.92
        )
    ]

    term: Annotated[
        Literal[36, 60],
        Field(
            description="Loan repayment duration in months. Typically 36 months (3 years) or 60 months (5 years).",
            example=60
        )
    ]

    int_rate: Annotated[
        float,
        Field(
            ge=0,
            le=40,
            description="Interest rate charged on the loan expressed as a percentage.",
            example=21.49
        )
    ]

    installment: Annotated[
        float,
        Field(
            gt=0,
            description="Monthly installment amount the borrower must pay to repay the loan.",
            example=557.53
        )
    ]

    grade: Annotated[
        Literal["A","B","C","D","E","F","G"],
        Field(
            description="Loan grade assigned by the lending platform based on borrower credit risk (A = lowest risk, G = highest risk).",
            example="D"
        )
    ]

    sub_grade: Annotated[
        Literal[
            "A1","A2","A3","A4","A5",
            "B1","B2","B3","B4","B5",
            "C1","C2","C3","C4","C5",
            "D1","D2","D3","D4","D5",
            "E1","E2","E3","E4","E5",
            "F1","F2","F3","F4","F5",
            "G1","G2","G3","G4","G5"
        ],
        Field(
            description="More detailed classification within each loan grade indicating finer risk segmentation.",
            example="D5"
        )
    ]

    purpose: Annotated[
        str,
        Field(
            description="Purpose for which the borrower is taking the loan (e.g., credit card repayment, debt consolidation, etc.). Unknown purposes will be mapped to 'other'.",
            example="credit_card"
        )
    ]

    application_type: Annotated[
        Literal["Individual","Joint App"],
        Field(
            description="Indicates whether the loan application was submitted by an individual borrower or jointly with another borrower.",
            example="Individual"
        )
    ]


    # Financial Features

    annual_inc: Annotated[
        float,
        Field(
            gt=0,
            description="Borrower's reported annual income (log-transformed value used in model training).",
            example=11.25
        )
    ]

    dti: Annotated[
        float,
        Field(
            ge=0,
            description="Debt-to-Income ratio representing the percentage of income used to pay existing debts.",
            example=29.27
        )
    ]

    verification_status: Annotated[
        Literal["Not Verified","Source Verified","Verified"],
        Field(
            description="Indicates whether the borrower's income was verified by the lending platform.",
            example="Verified"
        )
    ]

    home_ownership: Annotated[
        str,
        Field(
            description="Borrower's home ownership status (e.g., rent, own, mortgage). Unknown values are mapped to 'other'.",
            example="MORTGAGE"
        )
    ]

    emp_length: Annotated[
        str,
        Field(
            description="Length of employment of the borrower indicating job stability. Unknown values will be mapped to 'unknown'.",
            example="10+ years"
        )
    ]


    # Credit Behaviour

    acc_now_delinq: Annotated[
        int,
        Field(
            ge=0,
            description="Number of accounts currently delinquent (past due payments).",
            example=0
        )
    ]

    num_accts_ever_120_pd: Annotated[
        int,
        Field(
            ge=0,
            description="Number of accounts that have ever been 120 or more days past due.",
            example=0
        )
    ]

    num_tl_30dpd: Annotated[
        int,
        Field(
            ge=0,
            description="Number of accounts currently 30 days past due.",
            example=0
        )
    ]

    num_tl_90g_dpd_24m: Annotated[
        int,
        Field(
            ge=0,
            description="Number of accounts that were 90+ days delinquent in the last 24 months.",
            example=0
        )
    ]

    pct_tl_nvr_dlq: Annotated[
        float,
        Field(
            ge=0,
            le=100,
            description="Percentage of trade lines that have never been delinquent.",
            example=95.5
        )
    ]

    percent_bc_gt_75: Annotated[
        float,
        Field(
            ge=0,
            le=100,
            description="Percentage of bankcard accounts where utilization exceeded 75%.",
            example=0
        )
    ]

    bc_util: Annotated[
        float,
        Field(
            ge=0,
            le=100,
            description="Total bankcard utilization ratio representing how much credit is currently being used.",
            example=25.7
        )
    ]

    delinq_2yrs: Annotated[
        int,
        Field(
            ge=0,
            description="Number of delinquency events in the past 2 years.",
            example=0
        )
    ]

    inq_last_6mths: Annotated[
        int,
        Field(
            ge=0,
            description="Number of credit inquiries made in the last 6 months.",
            example=2
        )
    ]


    # Credit Structure

    open_acc: Annotated[
        int,
        Field(
            ge=0,
            description="Number of currently open credit accounts.",
            example=12
        )
    ]

    total_acc: Annotated[
        int,
        Field(
            ge=0,
            description="Total number of credit accounts in the borrower's credit history.",
            example=22
        )
    ]

    mort_acc: Annotated[
        int,
        Field(
            ge=0,
            description="Number of mortgage accounts the borrower currently has.",
            example=0
        )
    ]

    pub_rec: Annotated[
        int,
        Field(
            ge=0,
            description="Number of derogatory public records such as tax liens or judgments.",
            example=0
        )
    ]

    pub_rec_bankruptcies: Annotated[
        int,
        Field(
            ge=0,
            description="Number of bankruptcies recorded in public records.",
            example=0
        )
    ]


    # Credit Limits

    revol_bal: Annotated[
        float,
        Field(
            ge=0,
            description="Total revolving credit balance currently owed by the borrower.",
            example=5741
        )
    ]

    revol_util: Annotated[
        float,
        Field(
            ge=0,
            le=100,
            description="Revolving credit utilization rate indicating how much of available revolving credit is used.",
            example=3.09
        )
    ]

    tot_hi_cred_lim: Annotated[
        float,
        Field(
            ge=0,
            description="Total high credit limit across all credit accounts.",
            example=87879
        )
    ]

    total_bal_ex_mort: Annotated[
        float,
        Field(
            ge=0,
            description="Total balance on all accounts excluding mortgage balances.",
            example=52774
        )
    ]

    total_bc_limit: Annotated[
        float,
        Field(
            ge=0,
            description="Total credit limit across all bankcard accounts.",
            example=21200
        )
    ]

    total_rev_hi_lim: Annotated[
        float,
        Field(
            ge=0,
            description="Total revolving high credit limit across accounts.",
            example=27400
        )
    ]

    avg_cur_bal: Annotated[
        float,
        Field(
            ge=0,
            description="Average current balance across all credit accounts.",
            example=4398
        )
    ]

    il_util: Annotated[
        float,
        Field(
            ge=0,
            description="Installment loan utilization ratio indicating usage of installment credit.",
            example=78
        )
    ]

    max_bal_bc: Annotated[
        float,
        Field(
            ge=0,
            description="Maximum balance recorded on a bankcard account.",
            example=4847
        )
    ]

    
    @field_validator("purpose", mode="before")
    @classmethod
    def normalize_purpose(cls, value):

        value = str(value)

        # Normalize
        value = value.lower()
        value = value.replace(" ", "_")
        value = value.strip()

        # Unknown values → other
        if value not in ALLOWED_PURPOSES:
            return "other"

        return value
    
    @field_validator("application_type", mode="before")
    @classmethod
    def normalize_application_type(cls, value):

        value = str(value).lower().replace("_", " ").strip()

        if value == "individual":
            return "Individual"

        if value in ["joint app", "joint"]:
            return "Joint App"

        raise ValueError(
            "Invalid application_type. Allowed values: Individual or Joint App"
        )
    
    @field_validator("verification_status", mode="before")
    @classmethod
    def normalize_verification_status(cls, value):

        value = str(value).lower().replace("_", " ").strip()

        if value == "verified":
            return "Verified"

        if value == "not verified":
            return "Not Verified"

        if value == "source verified":
            return "Source Verified"

        raise ValueError(
            "Invalid verification_status. Allowed values: Verified, Not Verified, Source Verified"
        )
    

    @field_validator("home_ownership", mode="before")
    @classmethod
    def normalize_home_ownership(cls, value):

        value = str(value).lower().replace(" ", "_").strip()

        if value not in HOME_OWNERSHIP:
            return "other"

        return value
    
    @field_validator("emp_length", mode="before")
    @classmethod
    def normalize_emp_length(cls, value):

        value = str(value).lower().replace("_", " ").strip()

        # normalize common formats
        value = value.replace("years", "years")
        value = value.replace("year", "year")

        if value not in EMP_LENGTH_VALUES:
            return "unknown"

        return value
    
    
    
    
    
    # Feature Engineering
   

    @computed_field
    @property
    def loan_income_ratio(self) -> float:
        return self.loan_amnt / max(self.annual_inc, 1)

    @computed_field
    @property
    def installment_income_ratio(self) -> float:
        return self.installment / max(self.annual_inc, 1)

    @computed_field
    @property
    def total_credit_stress(self) -> float:
        return self.revol_bal / max(self.tot_hi_cred_lim, 1)

    @computed_field
    @property
    def delinquency_score(self) -> int:
        return (
            self.num_tl_90g_dpd_24m * 3 +
            self.num_tl_30dpd * 2 +
            self.acc_now_delinq
        )

    @computed_field
    @property
    def active_account_ratio(self) -> float:
        return self.open_acc / max(self.total_acc, 1)

    @computed_field
    @property
    def high_util_flag(self) -> int:
        return int(self.revol_util > 80)