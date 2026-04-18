import { DonationStatus, Money, DateTime, UUID } from './common';

/**
 * Donation campaign response object
 */
export interface DonationCampaign {
  id: UUID;
  title: string;
  description: string | null;
  goal_amount: Money;
  raised_amount: Money;
  donors_count: number | null;
  category: null;
  status: DonationStatus;
  image_url: string | null;
  start_date: DateTime;
  end_date: DateTime | null;
  progress: number;
  created_at: DateTime;
  updated_at: DateTime;
}

/**
 * Donation response object
 */
export interface Donation {
  id: UUID;
  campaign_id: UUID;
  donor_name: string | null;
  donor_email: string | null;
  amount: Money;
  payment_ref: string | null;
  created_at: DateTime;
}

/**
 * Create donation campaign request body
 */
export interface CreateCampaignBody {
  projectId: UUID;
  title: string;
  description?: string | null;
  goalCents: number;
  raisedCents?: number | null;
  donorCount?: number | null;
  status?: DonationStatus;
  coverImage?: string | null;
  startDate: DateTime;
  endDate?: DateTime | null;
}

/**
 * Update donation campaign request body
 */
export interface UpdateCampaignBody {
  title?: string;
  description?: string | null;
  goalCents?: number;
  raisedCents?: number | null;
  donorCount?: number | null;
  status?: DonationStatus;
  coverImage?: string | null;
  startDate?: DateTime;
  endDate?: DateTime | null;
}

/**
 * Campaign list query parameters
 */
export interface CampaignListParams {
  projectId?: UUID;
  search?: string;
  status?: DonationStatus;
  limit?: number;
  page?: number;
}

/**
 * Donation list query parameters
 */
export interface DonationListParams {
  projectId?: UUID;
  campaign_id?: UUID;
  search?: string;
  limit?: number;
  page?: number;
}

/**
 * Donation statistics response
 */
export interface DonationStats {
  totalCampaigns: number;
  activeCampaigns: number;
  totalRaised: Money;
  totalDonors: number;
  thisMonthDonations: Money;
  averageDonation: Money;
}
