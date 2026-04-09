//File was copied and modified from official Stripe documentation
const accountStatusEl = document.getElementById('account-status');

let accountStatus = null;
let accountId = accountStatusEl.dataset.stripeAccountId;

window.onload = () => {
    fetchAccountStatus();
}

async function fetchAccountStatus() {
  if (!accountId) return;

  try {
    const response = await fetch(`/member/account-status/${accountId}/`);
    if (!response.ok) {
      throw new Error('Failed to fetch account status');
    }
    accountStatus = await response.json();
    renderAccountStatus();

    // Show product form if account is ready
    if (accountStatus.chargesEnabled) {
      addProductBtn.classList.remove("hidden");
      productsSection.classList.remove('hidden');
      createAccountForm.classList.add("hidden");
    }
  } catch (error) {
    console.error('Error fetching account status:', error);
  }
}

function renderAccountStatus() {
  if (!accountStatus) return;

  const statusColor = accountStatus.chargesEnabled ? 'green' : 'orange';
  const statusText = accountStatus.chargesEnabled ? 'Active' : 'Pending';

  accountStatusEl.innerHTML = `
    <div class="account-status">
        <div class="spacer m-3">
            <hr class="color-platinum line-break full-length">
        </div>
      <div class="status-header">
        <h3>Account Status: <span style="color: ${statusColor}">${statusText}</span></h3>
      </div>
      <div class="status-details">
        <div class="status-item">
          <span>Account ID:</span>
          <span>${accountStatus.id}</span>
        </div>
        <div class="status-item">
          <span>Payouts enabled:</span>
          <span>${accountStatus.payoutsEnabled ? '✅' : '❌'}</span>
        </div>
        <div class="status-item">
          <span>Charges enabled:</span>
          <span>${accountStatus.chargesEnabled ? '✅' : '❌'}</span>
        </div>
        <div class="status-item">
          <span>Details submitted:</span>
          <span>${accountStatus.detailsSubmitted ? '✅' : '❌'}</span>
        </div>
      </div>
      ${needsOnboarding() ?
        `<button id="start-onboarding" class="btn btn-success">Onboard to collect payments</button>` : ''}
    </div>
  `;

  // Add event listeners to the new buttons
  if (needsOnboarding()) {
    document
    .getElementById('start-onboarding')
    .addEventListener('click', startOnboarding);
  }
}

function needsOnboarding() {
  return !accountStatus?.chargesEnabled && !accountStatus?.detailsSubmitted;
}

//Below 2 functions copied from official Stripe documentation and modified using Claude
async function startOnboarding() {
  try {
    const response = await fetch("/member/create-account-link/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),  // add this
      },
      body: JSON.stringify({ accountId }),
    });
    const { url } = await response.json();
    window.location.href = url;
  } catch (error) {
    console.error("Error starting onboarding:", error);
  }
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}